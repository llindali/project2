# Video recording walkthrough

These are AI-assisted recording scripts, not transcripts of completed recordings. Read each aloud once, use your own words where needed, and record only statements you understand and can support. After recording, correct the YouTube transcript to match the actual audio and save the actual transcript separately.

## Setup
1. Start the app with `python -m streamlit run app.py`. Leave it running while recording.
2. Set window to 60 months, fee to 0.25%, VT adjustment to 0 points and reserve to 3%.
3. Open browser tabs for the app, README, engine.py, app.py, validation record and visible output.
4. Use your screen recorder with microphone and screen capture. Close notifications and unrelated tabs. Rehearse once; timestamps below are targets, not claims about recorded durations.
5. For Video 1, open a calculator and actually perform `50000000 * 0.55` during the recording. The script calls this an arithmetic check, not independent validation of the whole engine.

| Video | Hard limit | Planned spoken duration | Files |
|---|---|---|---|
| 1: System evolution and checked AI output | 3:00 | About 2:30, plus short screen transitions | [Script 1](video-1-recording-script.txt) |
| 2: Code walkthrough | 5:00 | About 3:45–4:30 | [Script 2](video-2-recording-script.txt) |
| 3: Committee presentation | 5:00 | About 3:30–4:30, including controls | [Script 3](video-3-recording-script.txt) |

## Video 1 screen sequence
- 0:00–0:30: README and recommendation. Give both opening disclosures.
- 0:30–1:05: Base output and 36-month stress results.
- 1:05–1:45: Show calculator: 50,000,000 × 0.55 = 27,500,000, then match the reserve output.
- 1:45–2:40: Validation file: committed prediction, actual 60/0/40 result, and diagnosis.
- Finish before 3:00. The narrative describes the documented development; adapt any personal reflection to your actual experience.

## Video 2 screen sequence
- 0:00–0:25: README and opening disclosures.
- 0:25–1:15: engine.py: load_prices and signal.
- 1:15–2:00: estimates and measure.
- 2:00–3:10: run, especially candidate filters and lowest-volatility comparison.
- 3:10–3:45: stress_suite and saved output.
- 3:45–4:40: app.py control wiring and locked record.
- Scroll slowly enough that the function being explained is visible. You do not need to explain every import.

## Video 3 screen sequence
**Start with the live app already visible, not a title slide or GitHub page.**
- 0:00–1:10: Disclosures, rejection, mandate and assumptions.
- 1:10–2:00: Default three comparison rows; show hurdle and mandate verdict columns.
- 2:00–2:35: Change window 60 → 36. Show 80% SGOV / 20% VT and the 25-point stress stop.
- 2:35–3:15: Reset window to 60, then set VT adjustment to +1.5 points. Show 60% SGOV / 40% VT, return 7.34%, volatility 6.03%. Reset adjustment to zero.
- 3:15–4:40: Scroll to data card and stress table; explain limits, monitoring and committee ask.
- The stress table is a fixed suite; the main comparison responds to sidebar controls. Do not describe the suite as if it recalculates around every edited setting.

## After each recording
1. Check the actual duration against the hard limit; trim or rerecord if necessary.
2. Upload to YouTube and choose visibility your instructor can access; verify access while logged out.
3. Enable captions/transcripts and correct SGOV, BND, VT, CPI, percentages and attribution.
4. Save the actual spoken words as `docs/transcript-video-1.txt`, `docs/transcript-video-2.txt` and `docs/transcript-video-3.txt`. Scripts may help only after you reconcile them to the recording.
5. Send the three YouTube links, actual titles/durations and transcripts. The manifest can then be finalized with real timestamps.
