# 🔐 OPAQUE Login Authentication System

A secure authentication system implementing the **OPAQUE Password-Authenticated Key Exchange (PAKE)** protocol.

This project demonstrates how modern cryptographic authentication can eliminate the risks associated with traditional password-based login systems by ensuring that **passwords are never transmitted to or stored by the server in plaintext or as reusable secrets**.

---

## 📖 What is OPAQUE?

OPAQUE (Oblivious Password-Authenticated Key Exchange) is an asymmetric Password-Authenticated Key Exchange (aPAKE) protocol standardized by the IETF (RFC 9807).

Unlike traditional authentication methods where the server stores password hashes that can be stolen in a database breach, OPAQUE allows a client to authenticate **without ever revealing the password to the server**.

Even if an attacker compromises the server database, they cannot immediately perform offline dictionary attacks against user passwords.

---

## 🚀 Why OPAQUE?

Traditional authentication systems have several weaknesses:

- Password hashes can be stolen during database breaches.
- Attackers can perform offline brute-force attacks.
- Passwords may be exposed if TLS is compromised.
- Servers possess password-derived secrets that become valuable attack targets.

OPAQUE solves these problems by:

- ✅ Never sending the password to the server.
- ✅ Preventing offline dictionary attacks after database compromise.
- ✅ Ensuring the server never learns the user's password.
- ✅ Providing mutual authentication between client and server.
- ✅ Establishing a strong encrypted session key after authentication.

---

## ⚖️ OPAQUE vs Traditional Authentication

| Feature | Traditional Login | OPAQUE |
|----------|------------------|---------|
| Password sent to server | Yes (over TLS) | No |
| Server stores password hash | Yes | No reusable password secret |
| Offline dictionary attacks after DB leak | Possible | Resistant |
| Mutual authentication | Usually No | Yes |
| Session key establishment | Separate protocol | Built into authentication |

---

## 🛠 Technologies Used

- C++
- OPAQUE Protocol
- Cryptographic primitives
- Client-Server Authentication

---

## 📂 Project Structure

```
Opaque_Login/
│
├── client/         # Client-side authentication
├── server/         # Server-side authentication
├── include/        # Header files
├── src/            # Source code
└── README.md
```

*(Modify the structure above if your repository layout is different.)*

---

## 🔄 Authentication Workflow

1. User enters their password.
2. Client initiates the OPAQUE registration/login process.
3. Server responds without ever learning the user's password.
4. Client proves knowledge of the password.
5. Both parties derive the same secure session key.
6. Secure communication begins.

---

## 🔒 Security Benefits

- Password confidentiality
- Resistance to phishing attacks
- Protection against database breaches
- No plaintext password transmission
- Strong cryptographic session keys
- Forward secrecy (when combined with suitable key exchange)

---

## 🎯 Project Objectives

- Demonstrate a practical implementation of OPAQUE.
- Understand modern password-authenticated key exchange protocols.
- Explore secure alternatives to traditional password authentication.
- Learn advanced cryptographic authentication techniques.

---

## 📚 References

- **RFC 9807 — OPAQUE:** https://www.rfc-editor.org/rfc/rfc9807
- OPAQUE Specification: https://datatracker.ietf.org/doc/rfc9807/
- CFRG (Crypto Forum Research Group): https://datatracker.ietf.org/wg/cfrg/about/

---

## 👨‍💻 Author

**Shahnaz Aktar Mazumder**

B.Tech Computer Science & Engineering

GitHub: https://github.com/shhnzzzz

---

## ⭐ Future Improvements

- GUI-based client
- Multi-user authentication
- Persistent user database
- TLS integration
- Performance benchmarking
- Docker deployment
- Unit and integration testing

---

## 📜 License

This project is intended for educational and research purposes.
