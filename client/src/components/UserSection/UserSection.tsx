import {faCartShopping, faUser} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {Link, useNavigate} from "react-router-dom";
import {useTranslation} from "react-i18next";
import { myData, logout, isAuthenticated } from "../../utils/auth";
import type { UserData } from "../../utils/auth";
import "./UserSection.css";
import {useState, useEffect} from "react";



const UserSection = () => {
    const navigate = useNavigate();
    const [userData, setUserData] = useState<UserData | null>(null);
    const {t} = useTranslation();

    function toTitleCase(str: string): string {
        return str
            .split(' ')
            .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
            .join(' ');
    }


    const handleLogout = () => {
        logout()
        navigate('/login');
    }

    useEffect(() => {
        if (isAuthenticated()) {
            myData()
                .then((user) => {
                    console.log("User data:", user);
                    setUserData(user);
                })
                .catch((err) => {
                    console.error("Ошибка получения данных пользователя", err);
                    logout();
                    navigate("/login");
                });
        }
    }, []);


    return (
        <div className="user_section">
            {isAuthenticated() ? (
                <>
                    <div className="user_link_wrapper">
                        <Link to="/my-account" className="user_link">
                            <FontAwesomeIcon icon={faUser} className="user_icon"/>
                            <span>{userData
                                ? toTitleCase(`${userData.first_name} ${userData.last_name}`)
                                : "Loading..."}</span>
                        </Link>
                        <button className="logout_button" onClick={handleLogout}>
                            Logout
                        </button>
                    </div>
                </>
            ) : (
                <div className="user_account">
                    <div className="user_icon_block">
                        <FontAwesomeIcon icon={faUser} className="user_icon"/>
                    </div>
                    <div className="user_links">
                        <Link to="/login">{t("navbar.user_lt.0")}</Link>
                        <Link to="/registration">{t("navbar.user_lt.1")}</Link>
                    </div>
                </div>
            )}

            <Link to="/mycart">
                <FontAwesomeIcon icon={faCartShopping} className="cart-icon"/>
            </Link>
        </div>
    );
};

export default UserSection;
