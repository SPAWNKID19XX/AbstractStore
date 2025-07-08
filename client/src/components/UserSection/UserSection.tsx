import {useEffect, useState} from "react";
import {jwtDecode} from "jwt-decode";
import {faUser, faCartShopping} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {Link} from "react-router-dom";
import './UserSection.css';
import {useTranslation} from "react-i18next";

interface DecodedToken {
    username: string;
    email: string;
    exp: number;
    // другие поля, если есть
}

const UserSection = () => {
    const [user, setUser] = useState<DecodedToken | null>(null);
    const {t} = useTranslation();
    useEffect(() => {
        const token = localStorage.getItem("access");

        if (token) {
            try {
                const decoded = jwtDecode<DecodedToken>(token);
                setUser(decoded);
            } catch (error) {
                console.error("Invalid token", error);
                setUser(null);
            }
        } else {
            setUser(null);
        }
    }, []);

    return (
        <div className="user_section">
            {user ? (
                <>
                    <Link to="/myaccount" className="user_link">
                        <FontAwesomeIcon icon={faUser} className="user_icon"/>
                        <span>{user.email}</span>
                    </Link>
                </>
            ) : (
                <>
                    <div className="user_account">
                        <div className="user_icon_block">
                            <FontAwesomeIcon icon={faUser} className="user_icon"/>
                        </div>
                        <div className="user_links">
                            <Link to="/login">{t("navbar.user_lt.0")}</Link>
                            <Link to="/registration">{t("navbar.user_lt.1")}</Link>
                        </div>
                    </div>
                </>
            )}
            <Link to="/mycart">
                <FontAwesomeIcon icon={faCartShopping} className="cart-icon"/>
            </Link>
        </div>
    );
};

export default UserSection;