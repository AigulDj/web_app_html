
from playwright.sync_api import Page, expect

def test_get_albums(db_connection, page, test_web_address):
    db_connection.seed("seeds/record_store_html.sql")

    # We load a virtual browser and navigate to the /albums page
    page.goto(f"http://{test_web_address}/albums")
    # We look at all the <li> tags
    div_tags = page.locator("div")

    # We assert that it has the books in it
    expect(div_tags).to_have_text([
        "Title: Doolittle\nReleased: 1989",
        "Title: Surfer Rosa Released: 1988",
        "Title: Waterloo Released: 1974",
        "Title: Super Trouper Released: 1980",
        "Title: Bossanova Released: 1990",
        "Title: Lover Released: 2019",
        "Title: Folklore Released: 2020",
        "Title: I Put a Spell on You Released: 1965",
        "Title: Baltimore Released: 1978",
        "Title: Here Comes the Sun Released: 1971",
        "Title: Fodder on My Wings Released: 1982",
        "Title: Ring Ring Released: 1973"
    ])

def test_get_one_albums(db_connection, page, test_web_address):
    db_connection.seed("seeds/record_store_html.sql")

    # We load a virtual browser and navigate to the /albums page
    page.goto(f"http://{test_web_address}/albums/1")
    # We look at all the <li> tags
    div_tags = page.locator("div")

    # We assert that it has the books in it
    expect(div_tags).to_have_text(
        "Doolittle\nRelease year: 1989\nArtist: Pixies"
    )
