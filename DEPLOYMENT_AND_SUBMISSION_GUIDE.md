# Deployment and Submission Guide

Use this guide for the assignment screenshots and PDF submission.

## What To Submit

Create one Word file with two screenshots:

1. Your local computer browsing the Windows Server 2025 VM prototype.
2. Your local computer browsing the Ubuntu 24.04 LTS VM prototype.

Then convert the Word file to PDF and upload the PDF.

Better sentence for your assignment note:

> This is my individual initial prototype framework. The team will meet next week to compare all three individual prototypes and merge them into one finalized team version.

## Screenshot 1: Windows Server 2025 VM

1. Copy the `prototype` folder to the Windows Server 2025 VM.
2. Open PowerShell as Administrator.
3. Open HTTP and HTTPS ports:

```powershell
New-NetFirewallRule -DisplayName "AAR Prototype HTTP 80" -Direction Inbound -Protocol TCP -LocalPort 80 -Action Allow
New-NetFirewallRule -DisplayName "AAR Prototype HTTPS 443" -Direction Inbound -Protocol TCP -LocalPort 443 -Action Allow
```

4. Start the app:

```powershell
cd C:\Path\To\CapstoneProject\prototype
$env:HOST="0.0.0.0"
$env:PORT="80"
python .\backend\app.py
```

5. On your local computer, open:

```text
http://WINDOWS_SERVER_EXTERNAL_IP/
```

6. Generate a draft report and take a screenshot.

## Screenshot 2: Ubuntu 24.04 LTS VM

1. Copy the `prototype` folder to the Ubuntu VM.
2. Open the firewall if needed:

```bash
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
```

3. Start the app:

```bash
cd /path/to/CapstoneProject/prototype
export HOST=0.0.0.0
export PORT=80
sudo -E python3 backend/app.py
```

4. On your local computer, open:

```text
http://UBUNTU_EXTERNAL_IP/
```

5. Generate a draft report and take a screenshot.

## OpenAI API Key Option

The prototype runs without the key by using a mock fallback. To use the real API, set:

Windows:

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
$env:OPENAI_MODEL="auto"
```

Ubuntu:

```bash
export OPENAI_API_KEY="your_api_key_here"
export OPENAI_MODEL="auto"
```

Do not put your real API key in screenshots, Word files, PDFs, or GitHub.

## Organization Tips

- Save screenshots with clear names: `windows-server-prototype.png` and `ubuntu-prototype.png`.
- Put both screenshots in one Word file titled `Brittany_Initial_Prototype_Framework.docx`.
- Add one sentence under each screenshot naming the VM and URL used.
- Convert the Word file to PDF before uploading.
