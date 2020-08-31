export const items = [
  {
    text: "홈",
    model: false,
    children: [],
  },
  {
    text: "주문관리",
    model: false,
    children: [],
  },
  {
    iconAlt: "mdi-chevron-down",
    text: "상품 관리",
    model: false,
    children: [
      {
        text: "상품 등록",
        path: "admin/productRegistration",
      },
      {
        text: "상품 관리",
        path: "admin/productManagement",
      },
    ],
  },
  {
    text: "회원 관리",
    model: false,
    children: [
      {
        text: "회원 관리_커뮤니티",
        path: "seller/sellerregist",
      },
    ],
  },
];
