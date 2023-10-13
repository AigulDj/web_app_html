
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
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tags = page.locator("h1")
    p_tags = page.locator("p")

    expect(h1_tags).to_have_text(
        "Doolittle"
    )
    expect(p_tags).to_have_text([
        "Release year: 1989 Artist: Pixies"
    ])

def test_get_artists(db_connection, page, test_web_address):
    db_connection.seed("seeds/record_store_html.sql")
    page.goto(f"http://{test_web_address}/artists")
    h1_tags = page.locator("h1")

    expect(h1_tags).to_have_text([
        'Name: Pixies',
        'Name: ABBA',
        'Name: Taylor Swift',
        'Name: Nina Simone'
    ])

def test_get_single_artist(db_connection, page, test_web_address):
    db_connection.seed("seeds/record_store_html.sql")
    page.goto(f"http://{test_web_address}/artists/2")
    h2_tags = page.locator("h2")
    p_tags = page.locator("p")

    expect(h2_tags).to_have_text("Name: ABBA")
    expect(p_tags).to_have_text("Genre: Pop")

    