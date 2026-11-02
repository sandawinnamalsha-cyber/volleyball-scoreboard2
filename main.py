import flet as ft

def main(page: ft.Page):
    page.title = "Volleyball Scoreboard Pro"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 600

    # Variables
    teamA_score = 0
    teamB_score = 0
    teamA_sets = 0
    teamB_sets = 0
    current_set = 1
    set_results = ["-", "-", "-"]

    # UI Components
    set_text = ft.Text(value="Set: 1", size=18, weight=ft.FontWeight.BOLD)
    score_text_A = ft.Text(value="Team A: 0", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE)
    score_text_B = ft.Text(value="Team B: 0", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE)
    
    set1_text = ft.Text(value="Set 1: -", size=14)
    set2_text = ft.Text(value="Set 2: -", size=14)
    set3_text = ft.Text(value="Set 3: -", size=14)
    
    sets_won_text = ft.Text(value="Sets - A: 0 | B: 0", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.RED)
    status_text = ft.Text(value="", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE)

    def update_display():
        score_text_A.value = f"Team A: {teamA_score}"
        score_text_B.value = f"Team B: {teamB_score}"
        set_text.value = f"Set: {current_set}"
        set1_text.value = f"Set 1: {set_results[0]}"
        set2_text.value = f"Set 2: {set_results[1]}"
        set3_text.value = f"Set 3: {set_results[2]}"
        sets_won_text.value = f"Sets - A:{teamA_sets} | B:{teamB_sets}"
        page.update()

    def check_winner():
        nonlocal teamA_sets, teamB_sets
        won = None
        if teamA_score >= 25 and (teamA_score - teamB_score) >= 2:
            won = "A"
        elif teamB_score >= 25 and (teamB_score - teamA_score) >= 2:
            won = "B"
        
        if won:
            set_results[current_set - 1] = f"Team {won}"
            if won == 'A':
                teamA_sets += 1
            else:
                teamB_sets += 1
            
            status_text.value = f"Team {won} wins the set {current_set}"
            btn_a.disabled = True
            btn_b.disabled = True
            
            if teamA_sets == 2 or teamB_sets == 2:
                status_text.value = f"TEAM {won} WINS THE MATCH!!!"
                status_text.color = ft.Colors.GREEN
            
            update_display()

    def score_a(e):
        nonlocal teamA_score
        teamA_score += 1
        check_winner()
        update_display()

    def score_b(e):
        nonlocal teamB_score
        teamB_score += 1
        check_winner()
        update_display()

    def next_set(e):
        nonlocal teamA_score, teamB_score, current_set
        if current_set >= 3 or teamA_sets == 2 or teamB_sets == 2:
            return
        teamA_score = 0
        teamB_score = 0
        current_set += 1
        status_text.value = ""
        btn_a.disabled = False
        btn_b.disabled = False
        update_display()

    # Buttons
    btn_a = ft.ElevatedButton("Team A", bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE, on_click=score_a)
    btn_b = ft.ElevatedButton("Team B", bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE, on_click=score_b)
    btn_next = ft.ElevatedButton("Next Set", bgcolor=ft.Colors.ORANGE, color=ft.Colors.WHITE, on_click=next_set)
    btn_exit = ft.ElevatedButton("Exit", bgcolor=ft.Colors.RED, color=ft.Colors.WHITE, on_click=lambda e: page.window.close())

    # Adding components to page
    page.add(
        ft.Text("Volleyball Scoreboard", size=24, weight=ft.FontWeight.BOLD),
        set_text,
        ft.Divider(),
        score_text_A,
        score_text_B,
        ft.Row([set1_text, set2_text, set3_text], alignment=ft.MainAxisAlignment.CENTER),
        sets_won_text,
        status_text,
        ft.Divider(),
        ft.Row([btn_a, btn_b, btn_next, btn_exit], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main)

