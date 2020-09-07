export const items = [
  {
    listIcon: "fas fa-home",
    text: "홈",
    model: false,
    children: [],
  },
  {
    listIcon: "fas fa-shopping-cart",
    iconToggle: "fas fa-angle-left",
    text: "주문관리",
    model: false,
    children: [
      {
        text: "결제완료관리",
        path: "admin/orderManagement",
      },
    ],
  },
  {
    listIcon: "fas fa-home",
    iconToggle: "fas fa-angle-left",
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
    listIcon: "fas fa-user",
    iconToggle: "fas fa-angle-left",
    text: "회원 관리",
    model: false,
    children: [
      {
        text: "회원 관리_커뮤니티",
        path: "admin/userManagement",
      },
    ],
  },
];
