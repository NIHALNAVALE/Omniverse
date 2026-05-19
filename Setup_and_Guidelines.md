# NVIDIA Omniverse Kit App Template — Ubuntu Setup Guide

A personal installation log documenting the steps taken to get NVIDIA Omniverse Kit App Template running on Ubuntu with an RTX 3070 Ti.

---

## System Specs
- **GPU:** NVIDIA GeForce RTX 3070 Ti
- **OS:** Ubuntu (22.04 recommended)

---

## Step 1 — Install Build Tools

The build system requires `make` and other compiler tools:

```bash
sudo apt-get update
sudo apt-get install build-essential
```

---

## Step 2 — Install NVIDIA Drivers

### Check if GPU is detected
```bash
lspci | grep -i nvidia
```

### Check available drivers
```bash
ubuntu-drivers devices
```
This lists all compatible drivers for your GPU. Based on the output, driver **595** was selected.

### Install the driver
```bash
sudo apt-get install nvidia-driver-595
sudo reboot
```

### Verify driver installation
```bash
nvidia-smi
```

---

## Step 3 — Fix: NVIDIA-SMI Failed / Driver Not Communicating

If `nvidia-smi` returns an error after driver install:

### Check if Secure Boot is enabled
```bash
mokutil --sb-state
```

If it returns `SecureBoot enabled`, this is the problem. The NVIDIA kernel module cannot load with Secure Boot enabled.

### Fix: Disable Secure Boot in BIOS
1. Reboot into BIOS/UEFI (`Del`, `F2`, or `F10` on startup depending on motherboard)
2. Navigate to **Security** or **Boot** tab
3. Find **Secure Boot** → set to **Disabled**
   - Note: This is different from Fast Boot — make sure you disable Secure Boot specifically
4. Save and exit (`F10`)
5. After reboot, verify:
```bash
nvidia-smi
```

You should now see your GPU, driver version, and CUDA version listed.

---

## Step 4 — Clone the Kit App Template

```bash
git clone https://github.com/NVIDIA-Omniverse/kit-app-template.git
cd kit-app-template
```

---

## Step 5 — Create a New App

```bash
./repo.sh template new
```

Follow the interactive prompts:
- Accept the NVIDIA EULA
- Select template: **Kit Base Editor**
- Name your `.kit` file (e.g. `mycompany.my_editor`)
- Add application layer: **Yes → Default**

---

## Step 6 — Build

```bash
./repo.sh build
```

> First build downloads the Kit SDK and takes 10–20 minutes.

---

## Step 7 — Launch

```bash
./repo.sh launch
```

> On first launch, RTX shaders will compile for your GPU — this takes 10–30 minutes and shows 0.00% for a while. This is normal. Do not close the window.
> Subsequent launches are fast.

---

## Common Issues & Fixes

| Issue | Fix |
|---|---|
| `No such file or directory: 'make'` | `sudo apt-get install build-essential` |
| `nvidia-smi` fails after driver install | Disable Secure Boot in BIOS |
| RTX stuck at 0.00% on first launch | Wait 10–30 mins, shaders are compiling |
