// src/crypto/oprf.js

const PRIME = BigInt("57896044618658097711785492504343953926634992332820282019728792006155588075521");

const SERVER_SECRET = BigInt(12345);

export function hashPassword(password) {
    let hash = BigInt(0);

    for (let i = 0; i < password.length; i++) {
        hash += BigInt(password.charCodeAt(i));
    }

    return hash % PRIME;
}

export function blindPassword(password) {

    const point = hashPassword(password);

    const blindFactor = BigInt(
        Math.floor(Math.random() * 1000000) + 1
    );

    const blinded = (point * blindFactor) % PRIME;

    return {
        blinded,
        blindFactor
    };
}

function modInverse(a, m) {

    let m0 = m;

    let x0 = 0n;
    let x1 = 1n;

    if (m === 1n)
        return 0n;

    while (a > 1n) {

        let q = a / m;

        let t = m;

        m = a % m;

        a = t;

        t = x0;

        x0 = x1 - q * x0;

        x1 = t;

    }

    if (x1 < 0n)
        x1 += m0;

    return x1;

}
export function unblind(evaluated, blindFactor) {

    const inverse = modInverse(
        blindFactor,
        PRIME
    );

    return (
        BigInt(evaluated) * inverse
    ) % PRIME;

}