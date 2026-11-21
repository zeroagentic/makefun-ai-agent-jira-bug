from pathlib import Path

# One-line joke tuned for developer recognition, surprise, and economy.
JOKE = "My AI coding agent said, 'I found the bug.' I asked which one— it opened a Jira ticket titled: Me."

Path('/output/entry.txt').write_text(JOKE, encoding='utf-8')
