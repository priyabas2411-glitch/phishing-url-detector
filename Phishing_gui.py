import tkinter as tk
import requests

def check_url():
    url = entry.get().strip()
    result = ""
    score = 0

    if not url:
        output.config(text="Enter a URL")
        return

    # ---------------- ANALYSIS ---------------- #

    if "https" not in url:
        score += 30
        result += "❌ No HTTPS detected\n"

    if "@" in url:
        score += 20
        result += "⚠️ '@' symbol found\n"

    if len(url) > 75:
        score += 20
        result += "⚠️ URL too long\n"

    if "-" in url:
        score += 10
        result += "⚠️ Hyphen detected\n"

    if "login" in url or "bank" in url or "verify" in url:
        score += 20
        result += "⚠️ Suspicious keyword found\n"

    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            result += "✅ Website reachable\n"
        else:
            score += 20
            result += "⚠️ Suspicious response\n"
    except:
        score += 40
        result += "❌ Website NOT reachable\n"

    # ---------------- SCORE ---------------- #

    result += f"\n🎯 Risk Score: {score}\n"

    if score <= 30:
        result += "🟢 SAFE"
    elif score <= 70:
        result += "🟡 SUSPICIOUS"
    else:
        result += "🔴 DANGEROUS"

    output.config(text=result)


# ---------------- HACKER STYLE UI ---------------- #

window = tk.Tk()
window.title("Phishing URL Detector")
window.geometry("550x450")
window.config(bg="black")

title = tk.Label(
    window,
    text="PHISHING URL DETECTOR",
    font=("Courier", 18, "bold"),
    fg="lime",
    bg="black"
)
title.pack(pady=10)

entry = tk.Entry(
    window,
    width=50,
    font=("Courier", 12),
    bg="black",
    fg="lime",
    insertbackground="lime",
    highlightthickness=2,
    highlightbackground="lime"
)
entry.pack(pady=10)

btn = tk.Button(
    window,
    text="CHECK URL",
    font=("Courier", 12, "bold"),
    bg="red",
    fg="white",
    command=check_url
)
btn.pack(pady=10)

output = tk.Label(
    window,
    text="",
    font=("Courier", 12),
    fg="lime",
    bg="black",
    justify="left"
)
output.pack(pady=20)

footer = tk.Label(
    window,
    text="Cyber Security Tool • Python Project",
    font=("Courier", 10),
    fg="gray",
    bg="black"
)
footer.pack(side="bottom", pady=10)

window.mainloop()