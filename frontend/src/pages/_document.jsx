import Document, { Html, Head, Main, NextScript } from "next/document"
import { i18n } from "next-i18next"

class MyDocument extends Document {
  render() {
    const { locale } = this.props.__NEXT_DATA__
    const dir = locale === "ar" ? "rtl" : "ltr"
    const lang = locale === "ar" ? "ar" : "en"

    return (
      <Html dir={dir} lang={lang}>
        <Head>
          <link
            href="https://fonts.googleapis.com/css2?family=Noto+Naskh+Arabic&display=swap"
            rel="stylesheet"
          />
        </Head>
        <body className={locale === "ar" ? "font-arabic" : ""}>
          <Main />
          <NextScript />
        </body>
      </Html>
    )
  }
}

export default MyDocument