import { useState } from "react";
import { Link } from "react-router-dom";

import Input from "../components/Input";
import Button from "../components/Button";

import {
    registerStart,
    registerFinish
} from "../services/opaqueService";

import {
    blindPassword,
    unblind
} from "../crypto/oprf";


function Register() {

    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleRegister = async () => {

    try {

        const { blinded, blindFactor } = blindPassword(password);

        const startResponse = await registerStart({

            username,
            email,
            blinded_password: blinded.toString()

        });

        const sharedSecret = unblind(

            startResponse.evaluated_password,

            blindFactor

        );

        const finishResponse = await registerFinish({

            username,

            email,

            credential_record: sharedSecret.toString(),

            envelope: "TEMP_ENVELOPE",

            server_public_key:
                startResponse.server_public_key

        });

        alert(finishResponse.message);

        console.log(sharedSecret.toString());

    }

    catch(err){

        console.error(err);

    }

};
 return (

<div className="container">

    <div className="auth-card">

        <h1>OPAQUE Authentication</h1>

        <p className="subtitle">
            Create your secure account
        </p>

        <Input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e)=>setUsername(e.target.value)}
        />

        <Input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e)=>setEmail(e.target.value)}
        />

        <Input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e)=>setPassword(e.target.value)}
        />

        <Button
            text="Register"
            onClick={handleRegister}
        />

        <div className="footer">

            Already have an account?

            <Link to="/login">
                Login
            </Link>

        </div>

    </div>

</div>

);

}

export default Register; 