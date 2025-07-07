import { useState, useEffect, useCallback } from 'react';
import './NavBar.css';
import logo from "../../assets/react.svg";
import LanguageSelector from "../LanguageSelector/LanguageSelector.tsx";
import { useTranslation } from "react-i18next";
import { Link } from 'react-router-dom';

// Nav item interface
interface NavItem {
    id: number;
    name: string;
    link?: string;
    subItems?: { name: string; link: string }[];
}

const Navbar = () => {
    const [isMenuOpen, setIsMenuOpen] = useState(false);
    const [scrolled, setScrolled] = useState(false);
    const { t } = useTranslation();

    const navItems: NavItem[] = [
        { id: 1, name: t("navbar.links.1"), link: '/about_us/' },
        {
            id: 2,
            name: t("navbar.links.2"),
            link: '/services/',
            subItems: [
                { name: t("about_us.links.0"), link: '/services/lab/' },
                { name: t("about_us.links.1"), link: '/services/products/' },
            ]
        },
        {
            id: 3,
            name: t("navbar.links.3.title"),
            link: '/products/',
            subItems: [
                { name: t("navbar.links.3.subtitle.0"), link: '/products/hair-care/' },
                { name: t("navbar.links.3.subtitle.1"), link: '/products/face-body-care/' },
                { name: t("navbar.links.3.subtitle.2"), link: '/products/health-balance/' },
            ]
        },
        { id: 4, name: t("navbar.links.4"), link: '/contact/' }
    ];

    // Scroll effect
    useEffect(() => {
        const handleScroll = () => setScrolled(window.scrollY > 20);
        window.addEventListener('scroll', handleScroll);
        return () => window.removeEventListener('scroll', handleScroll);
    }, []);

    // Prevent body scroll on mobile menu
    useEffect(() => {
        document.body.style.overflow = isMenuOpen ? 'hidden' : '';
        return () => { document.body.style.overflow = ''; };
    }, [isMenuOpen]);

    const toggleMenu = useCallback(() => {
        setIsMenuOpen(prev => !prev);
    }, []);

    const closeMenu = useCallback(() => {
        setIsMenuOpen(false);
    }, []);

    return (
        <>
            <header className={`navbar ${scrolled ? 'navbar-scrolled' : ''}`}>
                <div className="navbar-background-blur"></div>
                <div className="navbar-container">
                    {/* Logo */}
                    <div className="navbar-logo">
                        <Link to="/">
                            <div className="logo-container">
                                <img id="toTop" src={logo} alt="logo" />
                            </div>
                        </Link>
                    </div>

                    {/* Mobile Language Selector */}
                    <div className="mobile-visible-language">
                        <div className="language-selector">
                            <LanguageSelector />
                        </div>
                    </div>

                    {/* Desktop Navigation */}
                    <nav className="desktop-links navbar-links">
                        <ul>
                            {navItems.map(item => (
                                <li key={item.id} className={item.subItems ? "has-submenu" : ""}>
                                    <Link to={item.link || "#"}>{item.name}</Link>
                                    {item.subItems && (
                                        <ul className="submenu">
                                            {item.subItems.map((subItem, index) => (
                                                <li key={index}>
                                                    <Link to={subItem.link}>{subItem.name}</Link>
                                                </li>
                                            ))}
                                        </ul>
                                    )}
                                </li>
                            ))}
                        </ul>
                    </nav>

                    {/* Desktop Actions */}
                    <div className="desktop-actions navbar-actions">
                        <div className="language-selector">
                            <LanguageSelector />
                        </div>
                    </div>

                    {/* Mobile Menu Button */}
                    <button
                        className="mobile-menu-button"
                        onClick={toggleMenu}
                        aria-label="Toggle menu"
                        aria-expanded={isMenuOpen}
                    >
                        <span className="hamburger-line"></span>
                        <span className="hamburger-line"></span>
                        <span className="hamburger-line"></span>
                    </button>
                </div>
            </header>

            {/* Mobile Menu */}
            <div className={`mobile-menu ${isMenuOpen ? 'active' : ''}`}>
                <div className="mobile-menu-container">
                    <div className="mobile-menu-header">
                        <div className="navbar-logo">
                            <Link to="/">
                                <div className="logo-container">
                                    <img src={logo} alt="logo" />
                                </div>
                            </Link>
                        </div>
                        <button
                            className="mobile-menu-close"
                            onClick={closeMenu}
                            aria-label="Close menu"
                        >
                            ✕
                        </button>
                    </div>
                    <nav className="mobile-nav">
                        <ul>
                            {navItems.map(item => (
                                <li key={item.id} className={item.subItems ? "has-submenu" : ""}>
                                    <Link to={item.link || "#"} onClick={closeMenu}>{item.name}</Link>
                                    {item.subItems && (
                                        <ul className="submenu">
                                            {item.subItems.map((subItem, index) => (
                                                <li key={index}>
                                                    <Link to={subItem.link} onClick={closeMenu}>{subItem.name}</Link>
                                                </li>
                                            ))}
                                        </ul>
                                    )}
                                </li>
                            ))}
                        </ul>
                    </nav>
                </div>
            </div>
        </>
    );
};

export default Navbar;
