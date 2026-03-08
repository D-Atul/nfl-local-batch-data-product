from pathlib import Path
import tempfile
import sys

from src.runner.run_local_batch import main


def test_pipeline_runs_end_to_end():

    with tempfile.TemporaryDirectory() as tmpdir:

        outputs_dir = Path(tmpdir) / "outputs"
        logs_dir = Path(tmpdir) / "logs"

        sys.argv = [
            "run_local_batch",
            "--input_csv",
            "data/raw/spreadspoke_scores.csv",
            "--outputs_dir",
            str(outputs_dir),
            "--logs_dir",
            str(logs_dir),
        ]

        exit_code = main()

        assert exit_code == 0

        assert (outputs_dir / "metrics/season_summaries.parquet").exists()
        assert (outputs_dir / "metrics/team_outcomes.parquet").exists()
        assert (outputs_dir / "metrics/venue_neutral_counts.parquet").exists()

        assert len(list(logs_dir.glob("run_*.json"))) == 1