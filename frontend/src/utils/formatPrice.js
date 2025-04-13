export const formatPrice = (amount, currency = "AED") => {
    return new Intl.NumberFormat("en-US", {
      style: "currency",
      currency,
      minimumFractionDigits: 0,
    }).format(amount);
  };

  export default formatPrice
  // Usage: formatPrice(299, "AED") => "AED 299"