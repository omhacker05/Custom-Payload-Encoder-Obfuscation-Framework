#!/usr/bin/env python3
"""Payload Encoder GUI with Tkinter"""
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import base64
import string
import random

class Encoder:
    @staticmethod
    def base64_encode(p):
        return base64.b64encode(p.encode()).decode()
    
    @staticmethod
    def rot13_encode(p):
        result = []
        for c in p:
            if 'a' <= c <= 'z':
                result.append(chr((ord(c) - ord('a') + 13) % 26 + ord('a')))
            elif 'A' <= c <= 'Z':
                result.append(chr((ord(c) - ord('A') + 13) % 26 + ord('A')))
            else:
                result.append(c)
        return ''.join(result)
    
    @staticmethod
    def xor_encode(p, key="SECRET"):
        return ''.join(f'\\x{ord(chr(ord(c) ^ ord(key[i % len(key)]))):02x}' for i, c in enumerate(p))
    
    @staticmethod
    def hex_encode(p):
        return ''.join(f'\\x{ord(c):02x}' for c in p)
    
    @staticmethod
    def unicode_encode(p):
        return ''.join(f'\\u{ord(c):04x}' for c in p)
    
    @staticmethod
    def random_insert(p, density=0.3):
        result = []
        for c in p:
            result.append(c)
            if random.random() < density:
                result.append(random.choice(string.ascii_letters))
        return ''.join(result)
    
    @staticmethod
    def char_split(p, sep='|'):
        return sep.join(p)
    
    @staticmethod
    def reverse_string(p):
        return p[::-1]

class Tester:
    def __init__(self):
        self.signatures = [
            'exec', 'eval', 'system', 'os.', 'import', 'subprocess',
            'cmd', 'powershell', 'bash', 'sh', 'rm', 'del', 'wget',
            'curl', 'nc', 'ncat', '/bin/', 'C:\\', 'cmd.exe'
        ]
    
    def test_detection(self, p):
        detected = [s for s in self.signatures if s.lower() in p.lower()]
        return {
            'detected': len(detected) > 0,
            'signatures': detected,
            'count': len(detected)
        }

class PayloadEncoderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Payload Encoder & Obfuscation Framework")
        self.root.geometry("1000x700")
        self.root.configure(bg="#1e1e1e")
        
        self.encoder = Encoder()
        self.tester = Tester()
        
        # Style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background="#1e1e1e")
        style.configure('TLabel', background="#1e1e1e", foreground="#ffffff")
        style.configure('TButton', font=("Arial", 10))
        style.configure('Title.TLabel', background="#1e1e1e", foreground="#00ff00", font=("Arial", 14, "bold"))
        
        self.setup_ui()
    
    def setup_ui(self):
        # Title
        title_frame = ttk.Frame(self.root)
        title_frame.pack(fill="x", padx=10, pady=10)
        
        title = ttk.Label(title_frame, text="🎯 Payload Encoder & Obfuscation Framework", style='Title.TLabel')
        title.pack(side="left")
        
        # Main container
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Left panel - Input
        left_panel = ttk.Frame(main_frame)
        left_panel.pack(side="left", fill="both", expand=True, padx=5)
        
        ttk.Label(left_panel, text="Enter Payload:", font=("Arial", 11, "bold")).pack(anchor="w", pady=(0, 5))
        
        self.payload_input = tk.Text(left_panel, height=8, width=45, bg="#2d2d2d", fg="#ffffff", 
                                      font=("Courier", 10), insertbackground="white")
        self.payload_input.pack(fill="both", expand=True, pady=(0, 10))
        
        # Buttons frame
        button_frame = ttk.Frame(left_panel)
        button_frame.pack(fill="x", pady=5)
        
        ttk.Button(button_frame, text="Load Demo", command=self.load_demo).pack(side="left", padx=2)
        ttk.Button(button_frame, text="Clear", command=self.clear_input).pack(side="left", padx=2)
        
        # Encoding options
        ttk.Label(left_panel, text="Encoding Methods:", font=("Arial", 11, "bold")).pack(anchor="w", pady=(10, 5))
        
        button_grid = ttk.Frame(left_panel)
        button_grid.pack(fill="x")
        
        self.buttons = {
            'base64': ttk.Button(button_grid, text="1. Base64", command=lambda: self.encode('base64')),
            'rot13': ttk.Button(button_grid, text="2. ROT13", command=lambda: self.encode('rot13')),
            'xor': ttk.Button(button_grid, text="3. XOR", command=lambda: self.encode('xor')),
            'hex': ttk.Button(button_grid, text="4. Hex", command=lambda: self.encode('hex')),
        }
        
        self.buttons['base64'].grid(row=0, column=0, padx=2, pady=2, sticky="ew")
        self.buttons['rot13'].grid(row=0, column=1, padx=2, pady=2, sticky="ew")
        self.buttons['xor'].grid(row=0, column=2, padx=2, pady=2, sticky="ew")
        self.buttons['hex'].grid(row=0, column=3, padx=2, pady=2, sticky="ew")
        
        for col in range(4):
            button_grid.grid_columnconfigure(col, weight=1)
        
        button_grid2 = ttk.Frame(left_panel)
        button_grid2.pack(fill="x", pady=(5, 0))
        
        self.buttons.update({
            'unicode': ttk.Button(button_grid2, text="5. Unicode", command=lambda: self.encode('unicode')),
            'random': ttk.Button(button_grid2, text="6. Random Insert", command=lambda: self.encode('random')),
            'split': ttk.Button(button_grid2, text="7. Char Split", command=lambda: self.encode('split')),
            'reverse': ttk.Button(button_grid2, text="8. Reverse", command=lambda: self.encode('reverse')),
        })
        
        self.buttons['unicode'].grid(row=0, column=0, padx=2, pady=2, sticky="ew")
        self.buttons['random'].grid(row=0, column=1, padx=2, pady=2, sticky="ew")
        self.buttons['split'].grid(row=0, column=2, padx=2, pady=2, sticky="ew")
        self.buttons['reverse'].grid(row=0, column=3, padx=2, pady=2, sticky="ew")
        
        for col in range(4):
            button_grid2.grid_columnconfigure(col, weight=1)
        
        # Special buttons
        special_frame = ttk.Frame(left_panel)
        special_frame.pack(fill="x", pady=(10, 5))
        
        ttk.Button(special_frame, text="9. Test Detection", command=self.test_detection).pack(side="left", padx=2, expand=True, fill="x")
        ttk.Button(special_frame, text="10. Compare All", command=self.compare_all).pack(side="left", padx=2, expand=True, fill="x")
        
        # Right panel - Output
        right_panel = ttk.Frame(main_frame)
        right_panel.pack(side="right", fill="both", expand=True, padx=5)
        
        ttk.Label(right_panel, text="Result:", font=("Arial", 11, "bold")).pack(anchor="w", pady=(0, 5))
        
        self.output_text = scrolledtext.ScrolledText(right_panel, height=35, width=45, bg="#2d2d2d", 
                                                      fg="#00ff00", font=("Courier", 9), insertbackground="white")
        self.output_text.pack(fill="both", expand=True, pady=(0, 10))
        
        # Copy button
        ttk.Button(right_panel, text="Copy Result", command=self.copy_result).pack(fill="x")
    
    def load_demo(self):
        self.payload_input.delete("1.0", tk.END)
        self.payload_input.insert("1.0", "os.system('whoami')")
    
    def clear_input(self):
        self.payload_input.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)
    
    def get_payload(self):
        payload = self.payload_input.get("1.0", tk.END).strip()
        if not payload:
            messagebox.showerror("Error", "Please enter a payload!")
            return None
        return payload
    
    def encode(self, method):
        payload = self.get_payload()
        if not payload:
            return
        
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        
        try:
            if method == 'base64':
                result = self.encoder.base64_encode(payload)
                self.output_text.insert(tk.END, f"[BASE64 ENCODING]\n\n{result}\n")
            
            elif method == 'rot13':
                result = self.encoder.rot13_encode(payload)
                self.output_text.insert(tk.END, f"[ROT13 SUBSTITUTION]\n\n{result}\n")
            
            elif method == 'xor':
                result = self.encoder.xor_encode(payload)
                self.output_text.insert(tk.END, f"[XOR ENCRYPTION]\n\n{result}\n")
            
            elif method == 'hex':
                result = self.encoder.hex_encode(payload)
                self.output_text.insert(tk.END, f"[HEX CONVERSION]\n\n{result}\n")
            
            elif method == 'unicode':
                result = self.encoder.unicode_encode(payload)
                self.output_text.insert(tk.END, f"[UNICODE ENCODING]\n\n{result}\n")
            
            elif method == 'random':
                result = self.encoder.random_insert(payload)
                self.output_text.insert(tk.END, f"[RANDOM CHARACTER INSERTION]\n\n{result}\n")
            
            elif method == 'split':
                result = self.encoder.char_split(payload)
                self.output_text.insert(tk.END, f"[CHARACTER SPLITTING]\n\n{result}\n")
            
            elif method == 'reverse':
                result = self.encoder.reverse_string(payload)
                self.output_text.insert(tk.END, f"[CHARACTER REVERSAL]\n\n{result}\n")
            
            # Test detection
            test = self.tester.test_detection(result)
            self.output_text.insert(tk.END, f"\n{'='*45}\n")
            self.output_text.insert(tk.END, f"Detection Status: {'DETECTED ❌' if test['detected'] else 'NOT DETECTED ✓'}\n")
            self.output_text.insert(tk.END, f"Signatures: {test['signatures']}\n")
            self.output_text.insert(tk.END, f"Count: {test['count']}\n")
        
        except Exception as e:
            self.output_text.insert(tk.END, f"Error: {str(e)}")
        
        self.output_text.config(state="disabled")
    
    def test_detection(self):
        payload = self.get_payload()
        if not payload:
            return
        
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        
        test = self.tester.test_detection(payload)
        
        self.output_text.insert(tk.END, "[DETECTION TEST]\n\n")
        self.output_text.insert(tk.END, f"Original Payload: {payload}\n\n")
        self.output_text.insert(tk.END, f"Detection Status: {'DETECTED ❌' if test['detected'] else 'NOT DETECTED ✓'}\n")
        self.output_text.insert(tk.END, f"Signatures Found: {test['signatures']}\n")
        self.output_text.insert(tk.END, f"Count: {test['count']}\n\n")
        self.output_text.insert(tk.END, "Tested Signatures:\n")
        self.output_text.insert(tk.END, ", ".join(self.tester.signatures))
        
        self.output_text.config(state="disabled")
    
    def compare_all(self):
        payload = self.get_payload()
        if not payload:
            return
        
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        
        self.output_text.insert(tk.END, "[COMPARISON OF ALL METHODS]\n\n")
        self.output_text.insert(tk.END, f"Original: {payload}\n\n")
        self.output_text.insert(tk.END, f"{'Method':<20} {'Detected':<15} {'Signatures':<10}\n")
        self.output_text.insert(tk.END, "-" * 50 + "\n\n")
        
        methods = {
            'Base64': self.encoder.base64_encode(payload),
            'ROT13': self.encoder.rot13_encode(payload),
            'XOR': self.encoder.xor_encode(payload),
            'Hex': self.encoder.hex_encode(payload),
            'Unicode': self.encoder.unicode_encode(payload),
            'Random Insert': self.encoder.random_insert(payload),
            'Char Split': self.encoder.char_split(payload),
            'Reverse': self.encoder.reverse_string(payload)
        }
        
        for method_name, encoded in methods.items():
            test = self.tester.test_detection(encoded)
            status = "YES ❌" if test['detected'] else "NO ✓"
            self.output_text.insert(tk.END, f"{method_name:<20} {status:<15} {test['count']:<10}\n")
        
        self.output_text.config(state="disabled")
    
    def copy_result(self):
        result = self.output_text.get("1.0", tk.END).strip()
        if result:
            self.root.clipboard_clear()
            self.root.clipboard_append(result)
            messagebox.showinfo("Success", "Result copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No result to copy!")

if __name__ == '__main__':
    root = tk.Tk()
    app = PayloadEncoderGUI(root)
    root.mainloop()
