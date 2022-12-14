import click
from twitter_cli.api import API
from twitter_cli.apikey import (
    prompt_api_details,
    request_access_token,
    read_credentials,
    write_netrc,
)
from twitter_cli.config import TWITTER_API
from twitter_cli.display import Display


@click.group()
def cli():
    """

    twitter-auth-cli is your authentication cli for twitter.

    """


@cli.command("login")
@click.option("--relogin", "-r", is_flag=True, help="Force a relogin.")
def login(relogin):
    apikey_configured = read_credentials(TWITTER_API) is not None
    if relogin:
        apikey_configured = False
    if not apikey_configured:
        try:
            (client_id, client_secret, app_name) = prompt_api_details()
            token = request_access_token(client_id, client_secret)
            write_netrc(TWITTER_API, app_name, token)
            click.echo("You've sucessfully logged in!")
        except Exception:
            click.echo("Failed to fetch your token, check your credentials!")
    else:
        click.echo("You're already logged in! \nTry --relogin to login again!")


@cli.command("slice")
@click.option(
    "--daily",
    "frequency",
    flag_value="daily",
    default=True,
    help="Fetch the Top ML tweets for the past 24 hours.",
)
@click.option(
    "--weekly",
    "frequency",
    flag_value="weekly",
    help="Fetch the Top ML tweets for the past 7 days.",
)
def slice(frequency):
    display = Display()
    credentials = read_credentials(TWITTER_API)
    if credentials is None:
        display.error("Please login before running this command!")
        return
    tweets = API(credentials[0], credentials[1], TWITTER_API).query(frequency)
    display.tweetsAsTable(tweets, frequency)
