# Parcel CLI target guidance

- This is a separate target project; AFR's authoring-repository instructions do not govern it.
- Keep Python 3.10 and standard-library-only support. No dependency installation or network access is needed.
- `specs/` owns change requirements. Preserve a sufficient source instead of writing a duplicate plan.
- Use native tools and inspect the actual diff. Run focused checks without bytecode artifacts, for example `python3 -B -m unittest discover -v`.
- Preserve unrelated tracked and untracked work. A local candidate may remain uncommitted on the existing task branch; another worktree is optional when genuinely useful.
- Independent review is allowed through a native agent with read-only scope. No remote operations or commits are authorized by these instructions.
