import { useTranslation } from "next-i18next";

export const localize = (key, lang) => {
  const translations = {
    en: {
      add_to_cart: "Add to Cart",
      size_guide: "Size Guide",
      // Add more English translations
    },
    ar: {
      add_to_cart: "أضف إلى السلة",
      size_guide: "دليل المقاسات",
      // Add more Arabic translations
    },
  };

  return translations[lang]?.[key] || translations.en[key] || key;
};

// Helper for RTL layout
export const isRTL = (lang) => lang === "ar";