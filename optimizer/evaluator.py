import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

TIMEOUT_SECONDS = 60

CURSOR_AGENT_PROMPT = """Read the file ./check. It is the output of an untuned code-dup detector. \
For each cluster, report whether you think the matches should be refactored to make the code more DRY. \
If so report YES for that cluster, else report NO. Also suggest one simple textual feature\
 or analysis that would help us do a better job of classifying clusters as needing refactoring. \
Output nice, tidy json like {"clusters": {"CLUSTER_0": "YES", "CLUSTER_1": "NO", [etc.]}, "suggestion": "[whatever]"}."""


@dataclass
class EvalResult:
    num_yes: int
    num_clusters: int
    suggestion: str


def count_clusters_in_file(path: Path) -> int:
    content = path.read_text()
    matches = re.findall(r"^CLUSTER_\d+:", content, re.MULTILINE)
    return len(matches)


def extract_json_from_output(output: str) -> dict:
    match = re.search(r"\{.*\}", output, re.DOTALL)
    if not match:
        raise ValueError(f"No JSON object found in output: {output[:500]}")
    return json.loads(match.group())


def evaluate(path: str) -> EvalResult:
    check_file = Path("check")

    subprocess.run(
        ["dryer", path, "--verbose", "--data"],
        stdout=check_file.open("w"),
        stderr=subprocess.PIPE,
        timeout=TIMEOUT_SECONDS,
        check=True,
    )

    num_clusters = count_clusters_in_file(check_file)
    if num_clusters == 0:
        return EvalResult(num_yes=0, num_clusters=0, suggestion="")

    result = subprocess.run(
        ["cursor-agent", "--model=opus-4.5", "--print", CURSOR_AGENT_PROMPT],
        capture_output=True,
        text=True,
        timeout=TIMEOUT_SECONDS,
        check=True,
    )

    parsed = extract_json_from_output(result.stdout)
    clusters = parsed.get("clusters", {})
    suggestion = parsed.get("suggestion", "")

    assert len(clusters) == num_clusters, (
        f"Cluster count mismatch: dryer found {num_clusters}, cursor-agent returned {len(clusters)}"
    )

    num_yes = sum(1 for v in clusters.values() if v.upper() == "YES")

    return EvalResult(num_yes=num_yes, num_clusters=num_clusters, suggestion=suggestion)
