def analyze_email(email):
    email_lower = email.lower()

    def check_password(email_lower):
        if "password" in email_lower:
            return 30, "Mentions password (credential theft)"
        return 0, None

    def check_verify(email_lower):
        if "verify" in email_lower:
            return 15, "Asks to verify information"
        return 0, None

    def check_urgency(email_lower):
        if "urgent" in email_lower or "immediate" in email_lower:
            return 10, "Uses urgent or pressure language"
        return 0, None

    def check_links(email_lower):
        if "http://" in email_lower or "https://" in email_lower or "www." in email_lower:
            return 20, "Contains a link"
        return 0, None

    def check_all_caps(email):
        caps_count = 0
        for word in email.split():
            if word.isupper() and len(word) >= 4:
                caps_count += 1

        if caps_count >= 3:
            return 10, "Excessive ALL CAPS words"
        return 0, None

    score = 0
    reasons = []

    checks = [check_password, check_verify, check_urgency, check_links, check_all_caps]

    for check in checks:
        points, reason = check(email_lower if check != check_all_caps else email)
        score += points
        if reason:
            reasons.append(reason)

    if score >= 60:
        level = "HIGH"
    elif score >= 30:
        level = "MEDIUM"
    else:
        level = "LOW"

    bar_length = 20
    filled = min(score // 5, bar_length)
    risk_bar = "█" * filled + "░" * (bar_length - filled)

    return score, level, risk_bar, reasons
