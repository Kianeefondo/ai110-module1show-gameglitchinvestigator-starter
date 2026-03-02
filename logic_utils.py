def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty.

    This mirrors the behavior in :mod:`app` and is used by the Streamlit
    interface to determine the secret number space.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    # fallback to the most generous range
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an integer guess.

    Returns
    -------
    ok : bool
        ``True`` when parsing succeeded and ``guess_int`` contains a number.
    guess_int : int | None
        The integer value when ``ok`` is ``True``; otherwise ``None``.
    error_message : str | None
        Human-readable error message when parsing failed.
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare *guess* against *secret* and return a tuple
    ``(outcome, message)``.

    *outcome* will be one of ``"Win"``, ``"Too High"`` or ``"Too Low"``.
    ``message`` is a short emoji-enhanced hint suitable for display.
    """
    # Numerize the secret if possible so comparisons behave as expected.
    try:
        secret_num = int(secret)
    except (ValueError, TypeError):
        try:
            secret_num = int(float(str(secret)))
        except Exception:
            # fall back to string comparisons
            s_guess = str(guess)
            s_secret = str(secret)
            if s_guess == s_secret:
                return "Win", "🎉 Correct!"
            if s_guess > s_secret:
                return "Too High", "📈 Go LOWER!"
            return "Too Low", "📉 Go HIGHER!"

    if guess == secret_num:
        return "Win", "🎉 Correct!"
    if guess > secret_num:
        return "Too High", "📈 Go LOWER!"
    return "Too Low", "📉 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update an ongoing score based on the latest guess result.

    Parameters
    ----------
    current_score : int
        The score prior to this guess.
    outcome : str
        One of ``"Win"``, ``"Too High"`` or ``"Too Low"``.
    attempt_number : int
        The 1‑based guess count for this round.
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
