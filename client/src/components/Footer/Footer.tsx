import styles from './Footer.module.css'
import {useTranslation} from "react-i18next";


const Footer = () => {
    const currentYear = new Date().getFullYear();
    const {t} = useTranslation();






    return (
        <div className={styles.footerContainer}>
            <section className={styles.footer}>
                <div className='footer-info'>
                    <div className={styles.contactPolitics}>
                        <div className={styles.contacts}>
                            <h3>{t("ftr.contact.title")}</h3>
                            <span>📞 (+000) 000 000 000</span>
                            <span>📧 email@gmail.com</span>
                            <span>📍 Address <br/> City zip-code</span>
                            {/*<button><img src={whatsapp} alt="" />{t("ftr.contact.btn")}</button>*/}
                        </div>
                        <div className={styles.politics}>
                            <h3>{t("ftr.docs.title")}</h3>
                            <a href="/privacy-policy">{t("ftr.docs.lt.0")}</a>
                            <a href="/cookie-policy">{t("ftr.docs.lt.1")}</a>
                            <a href="/terms-conditions">{t("ftr.docs.lt.2")}</a>
                        </div>
                    </div>
                </div>
            </section>
            <div className={styles.copyright}>
                <span>© {currentYear} BrandName. {t("ftr.bf")}.</span>
            </div>
        </div>
    )
}

export default Footer
