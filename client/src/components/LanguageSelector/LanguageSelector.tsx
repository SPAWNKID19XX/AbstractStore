import React from 'react';
import './LanguageSelector.css';
import { useTranslation } from "react-i18next";

interface Language {
    code: string;
    label: string;
    flag: string;
}

const languages: Language[] = [
    {
        code: 'pt',
        label: 'PT',
        flag: 'http://purecatamphetamine.github.io/country-flag-icons/3x2/PT.svg'
    },
    {
        code: 'en',
        label: 'EN',
        flag: 'http://purecatamphetamine.github.io/country-flag-icons/3x2/GB.svg'
    },
    {
        code: 'es',
        label: 'ES',
        flag: 'http://purecatamphetamine.github.io/country-flag-icons/3x2/ES.svg'
    },
    {
        code: 'it',
        label: 'IT',
        flag: 'http://purecatamphetamine.github.io/country-flag-icons/3x2/IT.svg'
    }
];

const LanguageSwitcher: React.FC = () => {
    const { i18n } = useTranslation();

    const handleLanguageChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
        i18n.changeLanguage(event.target.value);
    };

    const getCurrentLanguage = () => {
        console.log('current language',i18n.language)
        return languages.find(lang => lang.code === i18n.language) || languages[0];
    };

    return (
        <div className="language-dropdown">
            <select
                value={i18n.language}
                onChange={handleLanguageChange}
                className="language-select"
            >
                {languages.map((lang) => (
                    <option key={lang.code} value={lang.code}>
                        {lang.label}
                    </option>
                ))}
            </select>
            <img
                src={getCurrentLanguage().flag}
                alt={`${getCurrentLanguage().label} flag`}
                className="selected-flag"
            />
        </div>
    );
};

export default LanguageSwitcher;