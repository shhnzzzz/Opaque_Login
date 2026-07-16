import { useState } from "react";
import Input from "../components/Input";
import Button from "../components/Button";
import { Link } from "react-router-dom";

import {
  loginStart,
  loginFinish,
} from "../services/loginService";

import {
  blindPassword,
  unblind,
} from "../crypto/oprf";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    try {
      // Step 1: Blind the password
      const { blinded, blindFactor } = blindPassword(password);

      // Step 2: Send blinded password to server
      const startResponse = await loginStart({
        username,
        blinded_password: blinded.toString(),
      });

      // Step 3: Unblind the evaluated password
      const sharedSecret = unblind(
        startResponse.evaluated_password,
        blindFactor
      );

      // Step 4: Finish login
      const finishResponse = await loginFinish({
        username,
        shared_secret: sharedSecret.toString(),
      });

      alert(finishResponse.message);

      console.log("Shared Secret:", sharedSecret.toString());
      console.log(startResponse);
    } catch (error) {
      console.error(error);

      if (error.response) {
        alert(error.response.data.detail);
      } else {
        alert("Login Failed");
      }
    }
  };

return (

<div className="container">

    <div className="auth-card">

        <h1>OPAQUE Authentication</h1>

        <p className="subtitle">
            Secure Sign In
        </p>

        <Input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e)=>setUsername(e.target.value)}
        />

        <Input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e)=>setPassword(e.target.value)}
        />

        <Button
            text="Login"
            onClick={handleLogin}
        />

        <div className="footer">

            Don't have an account?

            <Link to="/">
                Register
            </Link>

        </div>

    </div>

</div>

);
}

export default Login;