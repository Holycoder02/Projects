import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

# ─── Color Palette ────────────────────────────────────────────────
BG_PRIMARY    = "#0f0f1a"
BG_SECONDARY  = "#1a1a2e"
BG_CARD       = "#16213e"
BG_INPUT      = "#1c2541"
ACCENT        = "#6c63ff"
ACCENT_HOVER  = "#817af7"
ACCENT_DARK   = "#4a42e0"
SUCCESS       = "#00c896"
WARNING       = "#ffb347"
DANGER        = "#ff6b6b"
TEXT_PRIMARY   = "#e8e8f0"
TEXT_SECONDARY = "#8888aa"
TEXT_MUTED     = "#555577"
BORDER         = "#2a2a4a"
HIGHLIGHT      = "#252545"

# Grade colors
GRADE_A  = "#00c896"
GRADE_B  = "#6c63ff"
GRADE_C  = "#ffb347"
GRADE_D  = "#ff8c42"
GRADE_F  = "#ff6b6b"

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.json")

def get_letter_grade(score):
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"

def get_grade_color(score):
    if score >= 90: return GRADE_A
    if score >= 80: return GRADE_B
    if score >= 70: return GRADE_C
    if score >= 60: return GRADE_D
    return GRADE_F

class StudentGradeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GradeVault — Student Grade Manager")
        self.root.geometry("1000x720")
        self.root.minsize(900, 650)
        self.root.configure(bg=BG_PRIMARY)

        # Data
        self.students = {}
        self.load_data()

        # Configure ttk styles
        self.setup_styles()

        # Build UI
        self.build_header()
        self.build_body()
        self.build_statusbar()

        # Initial refresh
        self.refresh_table()
        self.update_stats()

    # ─── Styles ───────────────────────────────────────────────────
    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Treeview
        self.style.configure("Custom.Treeview",
            background=BG_SECONDARY,
            foreground=TEXT_PRIMARY,
            fieldbackground=BG_SECONDARY,
            borderwidth=0,
            font=("Segoe UI", 11),
            rowheight=38,
        )
        self.style.configure("Custom.Treeview.Heading",
            background=BG_CARD,
            foreground=TEXT_SECONDARY,
            font=("Segoe UI Semibold", 10),
            borderwidth=0,
            relief="flat",
        )
        self.style.map("Custom.Treeview",
            background=[("selected", ACCENT_DARK)],
            foreground=[("selected", "#ffffff")],
        )
        self.style.map("Custom.Treeview.Heading",
            background=[("active", BORDER)],
        )

        # Scrollbar
        self.style.configure("Custom.Vertical.TScrollbar",
            background=BG_CARD,
            troughcolor=BG_SECONDARY,
            borderwidth=0,
            arrowsize=0,
        )

    # ─── Header ───────────────────────────────────────────────────
    def build_header(self):
        header = tk.Frame(self.root, bg=BG_SECONDARY, height=70)
        header.pack(fill="x")
        header.pack_propagate(False)

        # Left — branding
        left = tk.Frame(header, bg=BG_SECONDARY)
        left.pack(side="left", padx=24)

        tk.Label(left, text="◆", font=("Segoe UI", 22), fg=ACCENT, bg=BG_SECONDARY).pack(side="left")
        tk.Label(left, text=" GradeVault", font=("Segoe UI Semibold", 18), fg=TEXT_PRIMARY, bg=BG_SECONDARY).pack(side="left")
        tk.Label(left, text="  Student Grade Manager", font=("Segoe UI", 10), fg=TEXT_SECONDARY, bg=BG_SECONDARY).pack(side="left", padx=(6, 0))

        # Right — search
        right = tk.Frame(header, bg=BG_SECONDARY)
        right.pack(side="right", padx=24)

        tk.Label(right, text="🔍", font=("Segoe UI", 12), bg=BG_SECONDARY, fg=TEXT_SECONDARY).pack(side="left")
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", lambda *_: self.refresh_table())
        self.search_entry = tk.Entry(right, textvariable=self.search_var,
            font=("Segoe UI", 11), bg=BG_INPUT, fg=TEXT_PRIMARY,
            insertbackground=ACCENT, relief="flat", width=22,
            highlightthickness=1, highlightcolor=ACCENT, highlightbackground=BORDER)
        self.search_entry.pack(side="left", padx=(6, 0), ipady=5)
        self.search_entry.insert(0, "")
        # placeholder
        self._search_placeholder = True
        self._set_search_placeholder()
        self.search_entry.bind("<FocusIn>", self._search_focus_in)
        self.search_entry.bind("<FocusOut>", self._search_focus_out)

    def _set_search_placeholder(self):
        if not self.search_var.get():
            self._search_placeholder = True
            self.search_entry.config(fg=TEXT_MUTED)
            self.search_entry.delete(0, "end")
            self.search_entry.insert(0, "Search students…")

    def _search_focus_in(self, e):
        if self._search_placeholder:
            self.search_entry.delete(0, "end")
            self.search_entry.config(fg=TEXT_PRIMARY)
            self._search_placeholder = False

    def _search_focus_out(self, e):
        if not self.search_var.get().strip():
            self._set_search_placeholder()

    # ─── Body ─────────────────────────────────────────────────────
    def build_body(self):
        body = tk.Frame(self.root, bg=BG_PRIMARY)
        body.pack(fill="both", expand=True, padx=20, pady=(14, 6))

        # Left panel — form + stats
        left_panel = tk.Frame(body, bg=BG_PRIMARY, width=310)
        left_panel.pack(side="left", fill="y", padx=(0, 14))
        left_panel.pack_propagate(False)

        self.build_form(left_panel)
        self.build_stats(left_panel)

        # Right panel — table
        right_panel = tk.Frame(body, bg=BG_PRIMARY)
        right_panel.pack(side="left", fill="both", expand=True)

        self.build_table(right_panel)

    # ─── Form ─────────────────────────────────────────────────────
    def build_form(self, parent):
        card = tk.Frame(parent, bg=BG_CARD, highlightbackground=BORDER, highlightthickness=1)
        card.pack(fill="x", pady=(0, 12))

        # Card header
        hdr = tk.Frame(card, bg=BG_CARD)
        hdr.pack(fill="x", padx=18, pady=(16, 8))
        tk.Label(hdr, text="✦  Add / Update Student", font=("Segoe UI Semibold", 12),
                 fg=TEXT_PRIMARY, bg=BG_CARD).pack(anchor="w")

        sep = tk.Frame(card, bg=BORDER, height=1)
        sep.pack(fill="x", padx=18)

        # Name
        form = tk.Frame(card, bg=BG_CARD)
        form.pack(fill="x", padx=18, pady=(12, 0))

        tk.Label(form, text="STUDENT NAME", font=("Segoe UI Semibold", 8),
                 fg=TEXT_SECONDARY, bg=BG_CARD).pack(anchor="w")
        self.name_entry = tk.Entry(form, font=("Segoe UI", 11), bg=BG_INPUT, fg=TEXT_PRIMARY,
            insertbackground=ACCENT, relief="flat",
            highlightthickness=1, highlightcolor=ACCENT, highlightbackground=BORDER)
        self.name_entry.pack(fill="x", ipady=6, pady=(4, 0))

        # Grade
        form2 = tk.Frame(card, bg=BG_CARD)
        form2.pack(fill="x", padx=18, pady=(10, 0))

        tk.Label(form2, text="GRADE (0 – 100)", font=("Segoe UI Semibold", 8),
                 fg=TEXT_SECONDARY, bg=BG_CARD).pack(anchor="w")
        self.grade_entry = tk.Entry(form2, font=("Segoe UI", 11), bg=BG_INPUT, fg=TEXT_PRIMARY,
            insertbackground=ACCENT, relief="flat",
            highlightthickness=1, highlightcolor=ACCENT, highlightbackground=BORDER)
        self.grade_entry.pack(fill="x", ipady=6, pady=(4, 0))

        # Buttons row
        btn_frame = tk.Frame(card, bg=BG_CARD)
        btn_frame.pack(fill="x", padx=18, pady=(14, 16))

        self._make_button(btn_frame, "  ＋  Add  ", ACCENT, self.add_student).pack(side="left", expand=True, fill="x", padx=(0, 4))
        self._make_button(btn_frame, "  ✎  Update  ", "#2d8cf0", self.update_student).pack(side="left", expand=True, fill="x", padx=(4, 0))

        # Delete row
        btn_frame2 = tk.Frame(card, bg=BG_CARD)
        btn_frame2.pack(fill="x", padx=18, pady=(0, 16))

        self._make_button(btn_frame2, "  ✕  Delete Selected  ", DANGER, self.delete_student).pack(fill="x")

    # ─── Stats ────────────────────────────────────────────────────
    def build_stats(self, parent):
        card = tk.Frame(parent, bg=BG_CARD, highlightbackground=BORDER, highlightthickness=1)
        card.pack(fill="x", pady=(0, 0))

        hdr = tk.Frame(card, bg=BG_CARD)
        hdr.pack(fill="x", padx=18, pady=(14, 6))
        tk.Label(hdr, text="📊  Statistics", font=("Segoe UI Semibold", 12),
                 fg=TEXT_PRIMARY, bg=BG_CARD).pack(anchor="w")

        sep = tk.Frame(card, bg=BORDER, height=1)
        sep.pack(fill="x", padx=18)

        stats_inner = tk.Frame(card, bg=BG_CARD)
        stats_inner.pack(fill="x", padx=18, pady=(10, 16))

        # stat labels
        self.stat_total   = self._stat_row(stats_inner, "Total Students", "0")
        self.stat_avg     = self._stat_row(stats_inner, "Average Grade", "—")
        self.stat_highest = self._stat_row(stats_inner, "Highest Grade", "—")
        self.stat_lowest  = self._stat_row(stats_inner, "Lowest Grade", "—")
        self.stat_passing = self._stat_row(stats_inner, "Passing Rate", "—")

        # Grade distribution bar
        self.dist_frame = tk.Frame(card, bg=BG_CARD)
        self.dist_frame.pack(fill="x", padx=18, pady=(0, 16))
        tk.Label(self.dist_frame, text="GRADE DISTRIBUTION", font=("Segoe UI Semibold", 8),
                 fg=TEXT_SECONDARY, bg=BG_CARD).pack(anchor="w", pady=(0, 6))
        self.dist_canvas = tk.Canvas(self.dist_frame, height=18, bg=BG_INPUT,
                                      highlightthickness=0, bd=0)
        self.dist_canvas.pack(fill="x")

    def _stat_row(self, parent, label, value):
        row = tk.Frame(parent, bg=BG_CARD)
        row.pack(fill="x", pady=3)
        tk.Label(row, text=label, font=("Segoe UI", 10), fg=TEXT_SECONDARY, bg=BG_CARD).pack(side="left")
        val = tk.Label(row, text=value, font=("Segoe UI Semibold", 11), fg=TEXT_PRIMARY, bg=BG_CARD)
        val.pack(side="right")
        return val

    def update_stats(self):
        n = len(self.students)
        self.stat_total.config(text=str(n))
        if n == 0:
            self.stat_avg.config(text="—")
            self.stat_highest.config(text="—")
            self.stat_lowest.config(text="—")
            self.stat_passing.config(text="—")
            self.dist_canvas.delete("all")
            return

        grades = list(self.students.values())
        avg = sum(grades) / n
        hi = max(grades)
        lo = min(grades)
        passing = sum(1 for g in grades if g >= 60)

        self.stat_avg.config(text=f"{avg:.1f}")
        self.stat_highest.config(text=str(hi), fg=GRADE_A)
        self.stat_lowest.config(text=str(lo), fg=get_grade_color(lo))
        pct = (passing / n) * 100
        self.stat_passing.config(text=f"{pct:.0f}%", fg=SUCCESS if pct >= 70 else WARNING)

        # Distribution bar
        self.dist_canvas.delete("all")
        self.dist_canvas.update_idletasks()
        w = self.dist_canvas.winfo_width() or 260
        counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
        for g in grades:
            counts[get_letter_grade(g)] += 1
        colors = {"A": GRADE_A, "B": GRADE_B, "C": GRADE_C, "D": GRADE_D, "F": GRADE_F}
        x = 0
        for letter in ["A", "B", "C", "D", "F"]:
            if counts[letter] == 0:
                continue
            seg_w = (counts[letter] / n) * w
            self.dist_canvas.create_rectangle(x, 0, x + seg_w, 18, fill=colors[letter], outline="")
            if seg_w > 20:
                self.dist_canvas.create_text(x + seg_w / 2, 9, text=letter,
                    font=("Segoe UI Semibold", 8), fill="#ffffff")
            x += seg_w

    # ─── Table ────────────────────────────────────────────────────
    def build_table(self, parent):
        # Table header
        tbl_hdr = tk.Frame(parent, bg=BG_PRIMARY)
        tbl_hdr.pack(fill="x", pady=(0, 8))
        tk.Label(tbl_hdr, text="📋  All Students", font=("Segoe UI Semibold", 13),
                 fg=TEXT_PRIMARY, bg=BG_PRIMARY).pack(side="left")

        self.count_label = tk.Label(tbl_hdr, text="0 students", font=("Segoe UI", 10),
                                     fg=TEXT_SECONDARY, bg=BG_PRIMARY)
        self.count_label.pack(side="right")

        # Table frame
        tbl_frame = tk.Frame(parent, bg=BORDER)
        tbl_frame.pack(fill="both", expand=True)

        cols = ("name", "grade", "letter", "status")
        self.tree = ttk.Treeview(tbl_frame, columns=cols, show="headings",
                                  style="Custom.Treeview", selectmode="browse")

        self.tree.heading("name",   text="Student Name")
        self.tree.heading("grade",  text="Grade")
        self.tree.heading("letter", text="Letter")
        self.tree.heading("status", text="Status")

        self.tree.column("name",   width=220, minwidth=140)
        self.tree.column("grade",  width=80,  minwidth=60, anchor="center")
        self.tree.column("letter", width=70,  minwidth=50, anchor="center")
        self.tree.column("status", width=100, minwidth=70, anchor="center")

        scrollbar = ttk.Scrollbar(tbl_frame, orient="vertical", command=self.tree.yview,
                                   style="Custom.Vertical.TScrollbar")
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Bind selection to populate form
        self.tree.bind("<<TreeviewSelect>>", self._on_select)

        # Tag colors for alternating rows
        self.tree.tag_configure("even", background=BG_SECONDARY)
        self.tree.tag_configure("odd",  background=HIGHLIGHT)

    def _on_select(self, event):
        sel = self.tree.selection()
        if sel:
            vals = self.tree.item(sel[0], "values")
            self.name_entry.delete(0, "end")
            self.name_entry.insert(0, vals[0])
            self.grade_entry.delete(0, "end")
            self.grade_entry.insert(0, vals[1])

    # ─── CRUD ─────────────────────────────────────────────────────
    def _get_inputs(self):
        name = self.name_entry.get().strip()
        grade_str = self.grade_entry.get().strip()
        if not name:
            messagebox.showwarning("Input Required", "Please enter a student name.")
            return None, None
        try:
            grade = int(grade_str)
        except ValueError:
            messagebox.showwarning("Invalid Grade", "Grade must be a number between 0 and 100.")
            return None, None
        if not (0 <= grade <= 100):
            messagebox.showwarning("Invalid Grade", "Grade must be between 0 and 100.")
            return None, None
        return name, grade

    def add_student(self):
        name, grade = self._get_inputs()
        if name is None:
            return
        if name in self.students:
            messagebox.showwarning("Duplicate", f"'{name}' already exists! Use Update instead.")
            return
        self.students[name] = grade
        self.save_data()
        self.refresh_table()
        self.update_stats()
        self._clear_form()
        self._flash_status(f"✓ Added {name} with grade {grade}", SUCCESS)

    def update_student(self):
        name, grade = self._get_inputs()
        if name is None:
            return
        if name not in self.students:
            messagebox.showwarning("Not Found", f"'{name}' does not exist. Use Add instead.")
            return
        old = self.students[name]
        self.students[name] = grade
        self.save_data()
        self.refresh_table()
        self.update_stats()
        self._clear_form()
        self._flash_status(f"✓ Updated {name}: {old} → {grade}", "#2d8cf0")

    def delete_student(self):
        sel = self.tree.selection()
        if sel:
            name = self.tree.item(sel[0], "values")[0]
        else:
            name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("No Selection", "Select a student or enter a name to delete.")
            return
        if name not in self.students:
            messagebox.showwarning("Not Found", f"'{name}' does not exist.")
            return
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{name}'?"):
            del self.students[name]
            self.save_data()
            self.refresh_table()
            self.update_stats()
            self._clear_form()
            self._flash_status(f"✓ Deleted {name}", DANGER)

    # ─── Helpers ──────────────────────────────────────────────────
    def _clear_form(self):
        self.name_entry.delete(0, "end")
        self.grade_entry.delete(0, "end")
        self.name_entry.focus_set()

    def refresh_table(self):
        if not hasattr(self, "tree"):
            return
        for item in self.tree.get_children():
            self.tree.delete(item)

        query = self.search_var.get().strip().lower()
        if self._search_placeholder:
            query = ""

        filtered = {k: v for k, v in self.students.items() if query in k.lower()}
        sorted_students = sorted(filtered.items(), key=lambda x: x[0].lower())

        for i, (name, grade) in enumerate(sorted_students):
            letter = get_letter_grade(grade)
            status = "Pass" if grade >= 60 else "Fail"
            tag = "even" if i % 2 == 0 else "odd"
            self.tree.insert("", "end", values=(name, grade, letter, status), tags=(tag,))

        self.count_label.config(text=f"{len(filtered)} student{'s' if len(filtered) != 1 else ''}")

    def _make_button(self, parent, text, color, command):
        btn = tk.Label(parent, text=text, font=("Segoe UI Semibold", 10),
                       bg=color, fg="#ffffff", cursor="hand2", padx=10, pady=8)
        btn.bind("<Button-1>", lambda e: command())
        btn.bind("<Enter>", lambda e, b=btn, c=color: b.config(bg=self._lighten(c)))
        btn.bind("<Leave>", lambda e, b=btn, c=color: b.config(bg=c))
        return btn

    @staticmethod
    def _lighten(hex_color, factor=0.15):
        hex_color = hex_color.lstrip("#")
        r, g, b = int(hex_color[:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        r = min(255, int(r + (255 - r) * factor))
        g = min(255, int(g + (255 - g) * factor))
        b = min(255, int(b + (255 - b) * factor))
        return f"#{r:02x}{g:02x}{b:02x}"

    # ─── Status Bar ───────────────────────────────────────────────
    def build_statusbar(self):
        self.statusbar = tk.Label(self.root, text="Ready", font=("Segoe UI", 9),
                                   bg=BG_SECONDARY, fg=TEXT_SECONDARY, anchor="w", padx=20, pady=4)
        self.statusbar.pack(fill="x", side="bottom")

    def _flash_status(self, msg, color=TEXT_SECONDARY):
        self.statusbar.config(text=msg, fg=color)
        self.root.after(4000, lambda: self.statusbar.config(text="Ready", fg=TEXT_SECONDARY))

    # ─── Persistence ──────────────────────────────────────────────
    def save_data(self):
        try:
            with open(DATA_FILE, "w") as f:
                json.dump(self.students, f, indent=2)
        except Exception as e:
            messagebox.showerror("Save Error", f"Could not save data:\n{e}")

    def load_data(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r") as f:
                    self.students = json.load(f)
            except Exception:
                self.students = {}


# ─── Entry Point ──────────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()

    # Center window on screen
    root.update_idletasks()
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    w, h = 1000, 720
    x = (sw - w) // 2
    y = (sh - h) // 2
    root.geometry(f"{w}x{h}+{x}+{y}")

    # Set icon if possible
    try:
        root.iconbitmap(default="")
    except Exception:
        pass

    app = StudentGradeApp(root)
    root.mainloop()