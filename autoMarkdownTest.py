from pyquery import PyQuery as pq



d = pq(url="https://docs.google.com/forms/d/e/1FAIpQLScARubn0xADxkrHiVnR5KuPhw_15c73-OYUKm0y1ReLg3_X5Q/viewscore?viewscore=AE0zAgCT-jZSO6Q0V9hVanyanKBvEwIu_vVHeip-Eub1miwa7rj_q4yQB_CZV3guRc5mMmQ")


items = d.find('div div [class = "OxAavc"]')

incorrectAnswers = (["\n## " + pq(x).find('span[class="M7eMe"]').text() + "\n" + pq(x).find("div [class='muwQbd']").text() for x in items if pq(x).find('[class = "zS667"]').attr("aria-label") == "Incorrect"])

for i in incorrectAnswers:
    print(i)




