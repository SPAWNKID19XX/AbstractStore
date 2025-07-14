import {faUser, faCartShopping} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {Link} from "react-router-dom";
import {useTranslation} from "react-i18next";
import {useAuth} from "../../auth/authContext";
import "./UserSection.css";

const UserSection = () => {
    const {user, logout} = useAuth();
    const {t} = useTranslation();

    function toTitleCase(str: string): string {
        return str
            .split(' ')
            .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
            .join(' ');
    }


    return (
        <div className="user_section">
            {user ? (
                <>
                    <div className="user_link_wrapper">
                        <Link to="/myaccount" className="user_link">
                            <FontAwesomeIcon icon={faUser} className="user_icon"/>
                            <span>{toTitleCase(user.full_name)}</span>
                        </Link>
                        <button onClick={logout} className="logout_button">
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
