import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import pymem

ctk.set_default_color_theme("blue")
win = ctk.CTk()
win.title("OAR Trainer")
win.geometry("400x520")
win.resizable(False, False)

pm = None
module_base = None

def connect_game():
    """Funkcja łącząca z procesem gry."""
    global pm, module_base
    
    if pm and pm.process_handle:
        return True
        
    try:
        pm = pymem.Pymem("OAR-Win64-Shipping.exe")
        module_base = pm.base_address
        return True
    except pymem.exception.ProcessNotFound:
        messagebox.showerror("Błąd", "Gra (OAR-Win64-Shipping.exe) nie jest włączona!")
        return False
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się zainicjować: {e}\n(Upewnij się, że uruchamiasz jako Administrator)")
        return False


# --- AMMO LOGIC ---
def toggle_ammo():
    if ammo_active.get():
        if connect_game():
            print("[+] Ammo Freeze Activated")
            loop_ammo()
    else:
        print("[-] Ammo Freeze Deactivated")

def loop_ammo():
    if ammo_active.get() and pm:
        try:
            base_address = module_base + 0x4722D90
            offsets = [0x348, 0x5A8, 0x330, 0x20, 0x278, 0xA0, 0x2C4]
            
            addr = pm.read_longlong(base_address)
            for offset in offsets[:-1]:
                addr = pm.read_longlong(addr + offset)
                
            final_addr = addr + offsets[-1]
            pm.write_int(final_addr, 10000)
        except Exception:
            pass 
            
        win.after(100, loop_ammo) # Changed to win.after


# --- HP LOGIC ---
def toggle_hp():
    if hp_active.get():
        if connect_game():
            print("[+] HP Freeze Activated")
            loop_hp()
    else:
        print("[-] HP Freeze Deactivated")

def loop_hp():
    if hp_active.get() and pm:
        try:
            hp_base_offset = 0x4C2F3B0 
            hp_offsets = [0x518, 0x28, 0x8, 0xF40, 0x260, 0x20, 0x6B0] 
            
            base_address = module_base + hp_base_offset
            
            addr = pm.read_longlong(base_address)
            for offset in hp_offsets[:-1]:
                addr = pm.read_longlong(addr + offset)
                
            final_addr = addr + hp_offsets[-1]
            pm.write_int(final_addr, 1000000)
        except Exception:
            pass 
            
        win.after(100, loop_hp) 


# --- SPEED LOGIC ---
def toggle_speed():
    if speed_active.get():
        if connect_game():
            print("[+] Speed Freeze Activated")
            loop_speed()
    else:
        print("[-] Speed Freeze Deactivated")

def loop_speed():
    if speed_active.get() and pm:
        try:
            speed_base_offset = 0x4c2f3b0 
            speed_offsets = [0x180, 0x38, 0x0, 0x30, 0x2a0, 0x288, 0x18c]
            
            base_address = module_base + speed_base_offset
            
            addr = pm.read_longlong(base_address)
            for offset in speed_offsets[:-1]:
                addr = pm.read_longlong(addr + offset)
                
            final_addr = addr + speed_offsets[-1]
            pm.write_float(final_addr, 10000.0) 
        except Exception:
            pass 
            
        win.after(100, loop_speed) 

# --- JUMP LOGIC ---
def toggle_jump():
    if jump_active.get():
        if connect_game():
            print("[+] Jump Freeze Activated")
            loop_jump()
    else:
        print("[-] Jump Freeze Deactivated")

def loop_jump():
    if jump_active.get() and pm:
        try:
            jump_base_offset = 0x4c2f3b0 
            jump_offsets = [0x180, 0x38, 0x0, 0x30, 0x2a0, 0x288, 0x158]
            
            base_address = module_base + jump_base_offset
            
            addr = pm.read_longlong(base_address)
            for offset in jump_offsets[:-1]:
                addr = pm.read_longlong(addr + offset)
                
            final_addr = addr + jump_offsets[-1]
            pm.write_float(final_addr, 1000.0) 
        except Exception:
            pass 
            
        win.after(100, loop_jump) 

# --- CROUCH SPEED LOGIC ---
def toggle_crouchspeed():
    if crouchspeed_active.get():
        if connect_game():
            print("[+] Crouch Speed Freeze Activated")
            loop_crouchspeed()
    else:
        print("[-] Crouch Speed Freeze Deactivated")

def loop_crouchspeed():
    if crouchspeed_active.get() and pm:
        try:
            crouchspeed_base_offset = 0x4c2f3b0 
            crouchspeed_offsets = [0x180, 0x38, 0x0, 0x30, 0x2a0, 0x288, 0x190]
            
            base_address = module_base + crouchspeed_base_offset
            
            addr = pm.read_longlong(base_address)
            for offset in crouchspeed_offsets[:-1]:
                addr = pm.read_longlong(addr + offset)
                
            final_addr = addr + crouchspeed_offsets[-1]
            pm.write_float(final_addr, 10000.0) 
        except Exception:
            pass 
            
        win.after(100, loop_crouchspeed) 

# --- ACCELERATION LOGIC ---
def toggle_Acceleration():
    if acceleration_active.get():
        if connect_game():
            print("[+] Acceleration Freeze Activated")
            loop_Acceleration()
    else:
        print("[-] Acceleration Freeze Deactivated")

def loop_Acceleration():
    if acceleration_active.get() and pm:
        try:
            acceleration_base_offset = 0x4c2f3b0 
            acceleration_offsets = [0x180, 0x38, 0x0, 0x30, 0x2a0, 0x288, 0x1a0]
            
            base_address = module_base + acceleration_base_offset
            
            addr = pm.read_longlong(base_address)
            for offset in acceleration_offsets[:-1]:
                addr = pm.read_longlong(addr + offset)
                
            final_addr = addr + acceleration_offsets[-1]
            pm.write_float(final_addr, 10000.0) 
        except Exception:
            pass 
            
        win.after(100, loop_Acceleration) 


# --- FOV LOGIC ---
def toggle_Fov():
    if FOV_active.get():
        if connect_game():
            print("[+] FOV Activated")
            loop_fov()
    else:
        print("[-] FOV Deactivated")

def loop_fov():
    if FOV_active.get() and pm:
        try:
            FOV_base_offset = 0x4c2f3b0
            FOV_offsets = [0x30, 0xE8, 0xF8, 0x120, 0x0, 0x20, 0x6D4]
            
            base_address = module_base + FOV_base_offset
            
            addr = pm.read_longlong(base_address)
            for offset in FOV_offsets[:-1]:
                addr = pm.read_longlong(addr + offset)
                
            final_addr = addr + FOV_offsets[-1]
            pm.write_int(final_addr, 176)  
            print(f"[DEBUG] Successfully wrote FOV to allocation: {hex(final_addr)}")
        except Exception as e:
            print(f"[DEBUG] FOV Error: {e}") # This will expose a MemoryReadError if offsets are bad
            
        win.after(100, loop_fov)


# ----------------------------- #
ammo_active = tk.BooleanVar()
hp_active = tk.BooleanVar()
speed_active = tk.BooleanVar()
jump_active = tk.BooleanVar()
crouchspeed_active = tk.BooleanVar()
acceleration_active = tk.BooleanVar()
FOV_active = tk.BooleanVar()
# ----------------------------- # 

# --- UI Setup ---
lbl_title = ctk.CTkLabel(win, text="OAR External Menu", font=("Segoe UI", 22, "bold"))
lbl_title.pack(pady=(25, 5))

lbl_subtitle = ctk.CTkLabel(win, text="Warning!", font=("Segoe UI", 14, "bold"), text_color="red")
lbl_subtitle.pack(pady=(0, 0))

lbl_info = ctk.CTkLabel(win, text="when using speed don't press shift or it will reset to normal speed", font=("Segoe UI", 12), text_color="gray")
lbl_info.pack(pady=(0, 0))

frame_container = ctk.CTkFrame(win, fg_color="transparent")
frame_container.pack(fill="both", expand=True, padx=40)

btn_ammo = ctk.CTkCheckBox(frame_container, text="INF AMMO", font=("Segoe UI", 14, "bold"), variable=ammo_active, command=toggle_ammo)
btn_ammo.pack(pady=12, anchor="w")

btn_hp = ctk.CTkCheckBox(frame_container, text="SET HP", font=("Segoe UI", 14, "bold"), variable=hp_active, command=toggle_hp)
btn_hp.pack(pady=12, anchor="w")

btn_speed = ctk.CTkCheckBox(frame_container, text="SET SPEED", font=("Segoe UI", 14, "bold"), variable=speed_active, command=toggle_speed)
btn_speed.pack(pady=12, anchor="w")

btn_jump = ctk.CTkCheckBox(frame_container, text="SET JUMP", font=("Segoe UI", 14, "bold"), variable=jump_active, command=toggle_jump)
btn_jump.pack(pady=12, anchor="w")

btn_crouchspeed = ctk.CTkCheckBox(frame_container, text="SET CROUCH SPEED", font=("Segoe UI", 14, "bold"), variable=crouchspeed_active, command=toggle_crouchspeed)
btn_crouchspeed.pack(pady=12, anchor="w")

btn_acceleration = ctk.CTkCheckBox(frame_container, text="SET ACCELERATION", font=("Segoe UI", 14, "bold"), variable=acceleration_active, command=toggle_Acceleration)
btn_acceleration.pack(pady=12, anchor="w")

btn_customFOV = ctk.CTkCheckBox(frame_container, text="SET CUSTOM FOV", font=("Segoe UI", 14, "bold"), variable=FOV_active, command=toggle_Fov) # Added command here
btn_customFOV.pack(pady=12, anchor="w")

lbl_footer = ctk.CTkLabel(win, text="v1.0.0", font=("Segoe UI", 10), text_color="#555555")
lbl_footer.pack(pady=(0, 15))

win.mainloop()