function Button({ text, onClick }) {

    return (

        <button
            type="button"
            className="auth-btn"
            onClick={onClick}
        >
            {text}
        </button>

    );

}

export default Button;