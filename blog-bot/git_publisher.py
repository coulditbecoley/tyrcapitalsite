"""
git_publisher.py
Stages, commits, and pushes the new post and updated blog.html to GitHub.
"""

import subprocess
import os
from datetime import datetime, timezone

REPO_PATH = "/home/ubuntu/Tyr-Capital"


def run(cmd, cwd=REPO_PATH):
    """Run a shell command and return stdout. Raises on error."""
    result = subprocess.run(
        cmd, shell=True, cwd=cwd,
        capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {cmd}\nSTDERR: {result.stderr.strip()}")
    return result.stdout.strip()


def publish_post(post):
    """
    Stage the new post file and updated blog.html, then commit and push to GitHub main.
    """
    post_filepath = os.path.join(REPO_PATH, "posts", post["filename"])
    blog_html = os.path.join(REPO_PATH, "blog.html")

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    commit_msg = f"auto: daily blog post — {post['title'][:60]} [{today}]"

    print("[git_publisher] Staging files...")
    run(f'git add posts/{post["filename"]} blog.html')

    # Check if there's actually something to commit
    status = run("git status --porcelain")
    if not status:
        print("[git_publisher] Nothing to commit — files unchanged.")
        return False

    print(f"[git_publisher] Committing: {commit_msg}")
    run(f'git commit -m "{commit_msg}"')

    print("[git_publisher] Pushing to GitHub...")
    run("git push origin main")

    print(f"[git_publisher] Successfully published: {post['filename']}")
    return True


if __name__ == "__main__":
    test_post = {"filename": "test-post-bitcoin-holds-key-support.html", "title": "Test Post"}
    try:
        publish_post(test_post)
    except Exception as e:
        print(f"Git publish error: {e}")
