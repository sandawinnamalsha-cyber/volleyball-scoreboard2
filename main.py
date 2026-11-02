import flet as ft

def main(page: ft.Page):
    page.title = "Volleyball Scoreboard"
    page.bgcolor = ft.Colors.BLACK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    team_a_score = ft.Text("0", size=80, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
    team_b_score = ft.Text("0", size=80, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)

    score_a = 0
    score_b = 0

    def add_a(e):
        nonlocal score_a
        score_a += 1
        team_a_score.value = str(score_a)
        page.update()

    def sub_a(e):
        nonlocal score_a
        if score_a > 0:
            score_a -= 1
        team_a_score.value = str(score_a)
        page.update()

    def add_b(e):
        nonlocal score_b
        score_b += 1
        team_b_score.value = str(score_b)
        page.update()

    def sub_b(e):
        nonlocal score_b
        if score_b > 0:
            score_b -= 1
        team_b_score.value = str(score_b)
        page.update()

    def reset_all(e):
        nonlocal score_a, score_b
        score_a = 0
        score_b = 0
        team_a_score.value = "0"
        team_b_score.value = "0"
        page.update()

    page.add(
        ft.Column(
            [
                ft.Text("VOLLEYBALL", size=30, color=ft.Colors.with_opacity(0.7, ft.Colors.WHITE)),
                ft.Row(
                    [
                        ft.Column([ft.Text("TEAM A", color=ft.Colors.WHITE), team_a_score,
                                   ft.Row([ft.ElevatedButton("-", on_click=sub_a), ft.ElevatedButton("+", on_click=add_a)], alignment=ft.MainAxisAlignment.CENTER)], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        ft.Text(":", size=60, color=ft.Colors.WHITE),
                        ft.Column([ft.Text("TEAM B", color=ft.Colors.WHITE), team_b_score,
                                   ft.Row([ft.ElevatedButton("-", on_click=sub_b), ft.ElevatedButton("+", on_click=add_b)], alignment=ft.MainAxisAlignment.CENTER)], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.ElevatedButton("RESET", on_click=reset_all, bgcolor=ft.Colors.RED, color=ft.Colors.WHITE)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)
