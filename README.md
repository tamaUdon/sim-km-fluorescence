### What is this?
- Sample code for [VSJ2025 Summer](https://sites.google.com/view/vsj2025summer/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0?authuser=0) Poster 2p38.

### Abstact
- In this study, we proposed an excitation fluorescence simulation method based on a cross-sectional model derived from petal tissue structure and the Kubelka-Munk theory.
- We extended the existing Kubelka-Munk theory by adding a fluorescence term, enabling the simulation of fluorescence propagation.

### Prerequisite
- Python 3.13
- Please install [uv](https://docs.astral.sh/uv/) before running.

### Get Started
```
uv install
uv run python linear_eq.py
```
### Sample Output
<img width="400" height="200" alt="nonf_led" src="https://github.com/user-attachments/assets/4ece92d5-c40e-43ec-a8cf-d060dfc4e310" />
<img width="400" height="200" alt="nonf_d65" src="https://github.com/user-attachments/assets/2434fa56-4e17-43e7-ab13-6f47aade20a3" />
<img width="400" height="200" alt="Cm_led" src="https://github.com/user-attachments/assets/f57de3ce-b759-4667-a7ad-f33f3fa82632" />
<img width="400" height="200" alt="Cm_d65" src="https://github.com/user-attachments/assets/47a3a369-b331-4386-bcd3-8648ddec300b" />
<img width="400" height="200" alt="cloro_led" src="https://github.com/user-attachments/assets/de390649-6573-4bb1-afcc-e155110a9017" />
<img width="400" height="200" alt="cloro_d65" src="https://github.com/user-attachments/assets/0bc3d155-60b1-4709-804d-e7336b85977b" />

### Assumptions
- Fluorescence has absorption energy = emission energy.
- No recursive fluorescence.
- Fluorescence wavelength is the inverted shape of the absorption wavelength.

### The Kubelka-Munk extension formula we proposed
- Ultraviolet spectrum region
  
<img width="317" height="76" alt="スクリーンショット 2025-09-13 14 17 42" src="https://github.com/user-attachments/assets/61d4ad97-aada-43e9-baa9-111fae4e96b2" />

- Visible light spectrum region
  
<img width="419" height="76" alt="スクリーンショット 2025-09-13 14 17 34" src="https://github.com/user-attachments/assets/1a02ddc7-7b42-4ac2-896a-72c9afdfd804" /></br>

Simply added the “-" sign for the absorption term and the “+" sign for the emission term to the existing equation.
