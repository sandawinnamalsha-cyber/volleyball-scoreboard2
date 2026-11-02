import flet as ft

def main(page: ft.Page):
    page.title = "Volleyball Scoreboard Pro"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.AUTO

    teamA_score = 0
    teamB_score = 0
    teamA_sets = 0
    teamB_sets = 0
    current_set = 1
    set_results = ["-", "-", "-"]
    
    teamA_name = "Team A"
    teamB_name = "Team B"

    set_text = ft.Text(value="SET 1", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE_70)
    score_text_A = ft.Text(value="0", size=80, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_300, animate_scale=ft.Animation(300, ft.AnimationCurve.BOUNCE_OUT))
    score_text_B = ft.Text(value="0", size=80, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_300, animate_scale=ft.Animation(300, ft.AnimationCurve.BOUNCE_OUT))
    
    label_A = ft.Text(value="TEAM A", size=16, color=ft.Colors.BLUE_300, weight=ft.FontWeight.BOLD)
    label_B = ft.Text(value="TEAM B", size=16, color=ft.Colors.GREEN_300, weight=ft.FontWeight.BOLD)
    
    set1_text = ft.Text(value="Set 1: -", size=13, color=ft.Colors.WHITE_54)
    set2_text = ft.Text(value="Set 2: -", size=13, color=ft.Colors.WHITE_54)
    set3_text = ft.Text(value="Set 3: -", size=13, color=ft.Colors.WHITE_54)
    
    sets_won_text = ft.Text(value="Sets - A:0 | B:0", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.AMBER)
    status_text = ft.Text(value="Game On!", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_200, text_align=ft.TextAlign.CENTER)

    # Team Name Inputs
    def on_team_a_change(e):
        nonlocal teamA_name
        teamA_name = e.control.value if e.control.value else "Team A"
        label_A.value = teamA_name.upper()
        btn_a.text = f"{teamA_name} +1"
        page.update()

    def on_team_b_change(e):
        nonlocal teamB_name
        teamB_name = e.control.value if e.control.value else "Team B"
        label_B.value = teamB_name.upper()
        btn_b.text = f"{teamB_name} +1"
        page.update()

    input_team_a = ft.TextField(label="Team A Name", value="Team A", width=160, on_change=on_team_a_change, color=ft.Colors.WHITE)
    input_team_b = ft.TextField(label="Team B Name", value="Team B", width=160, on_change=on_team_b_change, color=ft.Colors.WHITE)

    def update_display():
        score_text_A.value = f"{teamA_score}"
        score_text_B.value = f"{teamB_score}"
        set_text.value = f"SET {current_set}"
        set1_text.value = f"S1: {set_results[0]}"
        set2_text.value = f"S2: {set_results[1]}"
        set3_text.value = f"S3: {set_results[2]}"
        sets_won_text.value = f"SETS - {teamA_name}:{teamA_sets} | {teamB_name}:{teamB_sets}"
        page.update()

    def check_winner():
        nonlocal teamA_sets, teamB_sets
        won = None
        won_name = ""
        if teamA_score >= 25 and (teamA_score - teamB_score) >= 2:
            won = "A"; won_name = teamA_name
        elif teamB_score >= 25 and (teamB_score - teamA_score) >= 2:
            won = "B"; won_name = teamB_name
        
        if won:
            set_results[current_set - 1] = f"{won_name} {teamA_score}-{teamB_score}"
            if won == 'A': teamA_sets += 1
            else: teamB_sets += 1
            status_text.value = f"{won_name} WINS SET {current_set}!"
            status_text.color = ft.Colors.GREEN_ACCENT_400
            btn_a.disabled = True; btn_b.disabled = True
            if teamA_sets == 2 or teamB_sets == 2:
                status_text.value = f"🏆 {won_name} WINS MATCH!!! 🏆"
                status_text.color = ft.Colors.YELLOW
                status_text.size = 22
            update_display()

    def score_a(e): 
        nonlocal teamA_score; teamA_score += 1; check_winner(); update_display()
    def score_b(e): 
        nonlocal teamB_score; teamB_score += 1; check_winner(); update_display()

    def next_set(e):
        nonlocal teamA_score, teamB_score, current_set
        if current_set >= 3 or teamA_sets == 2 or teamB_sets == 2: return
        teamA_score = 0; teamB_score = 0; current_set += 1
        status_text.value = "Game On!"; status_text.color = ft.Colors.PURPLE_200
        btn_a.disabled = False; btn_b.disabled = False; update_display()
    
    def reset_match(e):
        nonlocal teamA_score, teamB_score, teamA_sets, teamB_sets, current_set, set_results
        teamA_score = 0; teamB_score = 0; teamA_sets = 0; teamB_sets = 0; current_set = 1; set_results = ["-", "-", "-"]
        status_text.value = "New Match!"; status_text.color = ft.Colors.PURPLE_200
        btn_a.disabled = False; btn_b.disabled = False; update_display()

    btn_a = ft.ElevatedButton(f"{teamA_name} +1", bgcolor=ft.Colors.BLUE_600, color=ft.Colors.WHITE, width=160, height=50, on_click=score_a)
    btn_b = ft.ElevatedButton(f"{teamB_name} +1", bgcolor=ft.Colors.GREEN_600, color=ft.Colors.WHITE, width=160, height=50, on_click=score_b)
    btn_next = ft.ElevatedButton("Next Set", bgcolor=ft.Colors.ORANGE_700, color=ft.Colors.WHITE, width=150, on_click=next_set)
    btn_reset = ft.ElevatedButton("Reset", bgcolor=ft.Colors.RED_700, color=ft.Colors.WHITE, width=100, on_click=reset_match)

    page.add(
        ft.Container(
            content=ft.Column([
                ft.Text("🏐 VOLLEYBALL PRO", size=22, weight=ft.FontWeight.BOLD),
                ft.Row([input_team_a, input_team_b], alignment=ft.MainAxisAlignment.CENTER),
                set_text,
                ft.Divider(height=1, color=ft.Colors.WHITE_24),
                ft.Row([
                    ft.Column([label_A, score_text_A], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    ft.Text(":", size=40, color=ft.Colors.WHITE_24),
                    ft.Column([label_B, score_text_B], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                ], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                ft.Row([set1_text, set2_text, set3_text], alignment=ft.MainAxisAlignment.CENTER, spacing=15),
                sets_won_text,
                status_text,
                ft.Divider(height=1, color=ft.Colors.WHITE_24),
                ft.Row([btn_a, btn_b], alignment=ft.MainAxisAlignment.CENTER, spacing=15),
                ft.Row([btn_next, btn_reset], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=12),
            padding=20, bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.BLACK), border_radius=20, border=ft.border.all(1, ft.Colors.WHITE_24)
        )
    )

ft.run(main)
