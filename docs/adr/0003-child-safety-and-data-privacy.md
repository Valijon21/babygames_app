# 3. Child Safety, Privacy-by-Design, and Data Minimization

Date: 2026-10-15  
Status: Accepted  

## Context
Bolajon is built for children starting from age 2 up to school ages. Child data protection laws (such as COPPA, GDPR-K, and ethical standards) require strict minimization of personal identifiable information (PII).

## Decision
1. **Accounts:** Children do NOT have independent login accounts or email credentials. All accounts belong strictly to Parents/Guardians.
2. **Child Profiles:** Contain only an alias/nickname, an age band (e.g. 2-4, 5-7, 8-10), and selected avatar key. No exact birthdate, location, device identifiers, or biometric data.
3. **Data Access & Isolation:** All endpoints enforcing ChildProfile access strictly verify Guardian ownership via DRF object-level permissions (`IsGuardianOfChild`).
4. **Third Parties & Monetization:** Absolutely zero third-party tracking scripts, zero behavioral ads, zero analytics SDKs that collect persistent identifiers from minors, and zero open public chat.
5. **Data Deletion:** Guardians have an explicit self-service mechanism to delete their child's profiles and associated game sessions permanently.

## Consequences
- Guaranteed compliance with child privacy best practices.
- High trust among parents and educational institutions.
