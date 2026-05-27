import sys
from playwright.sync_api import sync_playwright

APPS = [
    "https://telecom-churn-survival-santiagomuru.streamlit.app",
    "https://customer-review-intelligence-santiagomuru.streamlit.app",
    "https://customer-clv-prediction-santiagomuru.streamlit.app",
    "https://tokyo-real-estate-explorer-santiagomuru.streamlit.app",
    "https://telecom-churn-prediction-santiagomuru.streamlit.app",
    "https://uplift-marketing-incrementality-santiagomuru.streamlit.app",
]

WAKE_SELECTOR = 'button:has-text("Yes, get this app back up!")'


def wake(page, url):
    print(f"\n=== {url} ===", flush=True)
    try:
        page.goto(url, timeout=60_000, wait_until="domcontentloaded")
    except Exception as e:
        print(f"goto failed: {e}", flush=True)
        return False

    try:
        btn = page.locator(WAKE_SELECTOR).first
        btn.wait_for(state="visible", timeout=8_000)
        print("App was sleeping. Clicking wake button...", flush=True)
        btn.click()
        page.wait_for_timeout(45_000)
    except Exception:
        print("No wake button (already awake).", flush=True)
        page.wait_for_timeout(10_000)

    print("Done.", flush=True)
    return True


def main():
    failed = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context()
        page = ctx.new_page()
        for url in APPS:
            ok = wake(page, url)
            if not ok:
                failed.append(url)
        browser.close()

    if failed:
        print(f"\nFailed: {failed}", flush=True)
        sys.exit(1)
    print("\nAll apps awake.", flush=True)


if __name__ == "__main__":
    main()
