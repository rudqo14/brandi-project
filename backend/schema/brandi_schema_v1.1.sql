drop database brandi;

create database brandi character set utf8mb4 collate utf8mb4_general_ci;
use brandi;

-- products Table Create SQL
CREATE TABLE products
(
    `product_no`  INT         NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `created_at`  DATETIME    NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시', 
    `is_deleted`  TINYINT     NOT NULL    DEFAULT FALSE COMMENT '삭제여부', 
    PRIMARY KEY (product_no)
);

INSERT INTO products
(
    product_no
) VALUES (
    1
);

-- colors Table Create SQL
CREATE TABLE colors
(
    `color_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `name`      VARCHAR(50)    NOT NULL    COMMENT '색상명', 
    PRIMARY KEY (color_no)
);

ALTER TABLE colors COMMENT '색상 옵션';

INSERT INTO colors
(
    color_no,
    name
) VALUES (
    1,
    '블랙'
), (
    2,
    '화이트'
), (
    3,
    '그레이'
), (
    4,
    '아이보리'
), (
    5,
    '네이비'
), (
    6,
    '블루'
), (
    7,
    '레드'
), (
    8,
    '핑크'
), (
    9,
    '옐로우'
), (
    10,
    '베이지'
), (
    11,
    '연청'
), (
    12,
    '민트'
), (
    13,
    '진청'
), (
    14,
    '연베이지'
), (
    15,
    '중청'
), (
    16,
    '소라'
), (
    17,
    '그린'
), (
    18,
    '연퍼플'
), (
    19,
    '머스터드'
), (
    20,
    '퍼플'
), (
    21,
    '청록'
), (
    22,
    '딥핑크'
), (
    23,
    '인디핑크'
), (
    24,
    '딥그린'
), (
    25,
    '카키'
), (
    26,
    '와인'
), (
    27,
    '브라운'
), (
    28,
    '실버'
), (
    29,
    '크림'
), (
    30,
    '차콜'
), (
    31,
    '오렌지'
), (
    32,
    '올리브'
), (
    33,
    '라이트베이지'
), (
    34,
    '다크베이지'
), (
    35,
    '골드'
), (
    36,
    '라임'
), (
    37,
    '라이트블루'
), (
    38,
    '피치핑크'
), (
    39,
    '오트밀'
);


-- sizes Table Create SQL
CREATE TABLE sizes
(
    `size_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `name`     VARCHAR(50)    NOT NULL    COMMENT '사이즈명', 
    PRIMARY KEY (size_no)
);

ALTER TABLE sizes COMMENT '사이즈 옵션';

INSERT INTO sizes
(
    size_no,
    name
) VALUES (
    1,
    'Free'
), (
    2,
    'XL'
), (
    3,
    'L'
), (
    4,
    'M'
), (
    5,
    'S'
), (
    6,
    'XS'
), (
    7,
    25
), (
    8,
    26
), (
    9,
    27
), (
    10,
    28
), (
    11,
    29
), (
    12,
    30
), (
    13,
    32
), (
    14,
    34
), (
    15,
    35
), (
    16,
    36
), (
    17,
    37
), (
    18,
    38
), (
    19,
    39
), (
    20,
    40
), (
    21,
    85
), (
    22,
    90
), (
    23,
    95
), (
    24,
    100
), (
    25,
    105
), (
    26,
    'XXL'
), (
    27,
    'XXXL'
), (
    28,
    'XXXXL'
), (
    29,
    'M(44-55)'
), (
    30,
    'L(55-66)'
), (
    31,
    'L(55-마른66)'
), (
    32,
    210
), (
    33,
    215
), (
    34,
    220
), (
    35,
    225
), (
    36,
    230
), (
    37,
    235
), (
    38,
    240
), (
    39,
    245
), (
    40,
    250
), (
    41,
    255
), (
    42,
    260
), (
    43,
    265
), (
    44,
    270
), (
    45,
    275
), (
    46,
    280
), (
    47,
    285
), (
    48,
    290
), (
    49,
    '1호'
), (
    50,
    '2호'
), (
    51,
    '3호'
), (
    52,
    '4호'
), (
    53,
    '5호'
), (
    54,
    '6호'
), (
    55,
    '7호'
), (
    56,
    '8호'
), (
    57,
    '9호'
), (
    58,
    '10호'
), (
    59,
    '11호'
), (
    60,
    '12호'
), (
    61,
    '13호'
), (
    62,
    '14호'
), (
    63,
    '15호'
), (
    64,
    '16호'
), (
    65,
    '17호'
), (
    66,
    '18호'
), (
    67,
    '19호'
), (
    68,
    '70a'
), (
    69,
    '70b'
), (
    70,
    '70c'
), (
    71,
    '70d'
), (
    72,
    '70e'
), (
    73,
    '70f'
), (
    74,
    '70g'
), (
    75,
    '75a'
), (
    76,
    '75b'
), (
    77,
    '75c'
), (
    78,
    '75d'
), (
    79,
    '75e'
), (
    80,
    '75f'
), (
    81,
    '75g'
), (
    82,
    '80a'
), (
    83,
    '80b'
), (
    84,
    '80c'
), (
    85,
    '80d'
), (
    86,
    '80e'
), (
    87,
    '80f'
), (
    88,
    '80g'
), (
    89,
    '85a'
), (
    90,
    '85b'
), (
    91,
    '85c'
), (
    92,
    '85d'
), (
    93,
    '85e'
), (
    94,
    '85f'
), (
    95,
    '85g'
), (
    96,
    '90a'
), (
    97,
    '90b'
), (
    98,
    '90c'
), (
    99,
    '90d'
), (
    100,
    '90e'
), (
    101,
    '90f'
), (
    102,
    '90g'
), (
    103,
    '95a'
), (
    104,
    '95b'
), (
    105,
    '95c'
), (
    106,
    '95d'
), (
    107,
    '95e'
), (
    108,
    '95f'
), (
    109,
    '95g'
), (
    110,
    '100a'
), (
    111,
    '100b'
), (
    112,
    '100c'
), (
    113,
    '100d'
), (
    114,
    '100e'
), (
    115,
    '100f'
), (
    116,
    '100g'
), (
    117,
    '105a'
), (
    118,
    '105b'
), (
    119,
    '105c'
), (
    120,
    '105d'
), (
    121,
    '105e'
), (
    122,
    '105f'
), (
    123,
    '105g'
), (
    124,
    '아이폰8'
), (
    125,
    '아이폰8플러스'
), (
    126,
    '아이폰X'
), (
    127,
    '갤럭시S9'
), (
    128,
    '갤럭시S9플러스'
);

-- social_networks Table Create SQL
CREATE TABLE social_networks
(
    `social_network_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `name`               VARCHAR(45)    NOT NULL    COMMENT '소셜 이름', 
    PRIMARY KEY (social_network_no)
);

INSERT INTO social_networks
(
    social_network_no,
    name
) VALUES (
    1,
    'Google'
);

-- users Table Create SQL
CREATE TABLE users
(
    `user_no`         INT             NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `name`            VARCHAR(50)     NOT NULL    COMMENT '회원명', 
    `email`           VARCHAR(255)    NOT NULL    UNIQUE COMMENT '이메일',
    `password`        VARCHAR(50)     NULL        COMMENT '비밀번호', 
    `created_at`      DATETIME        NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '등록일', 
    `last_access`     DATETIME        NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '최종접속일', 
    `social_id`       INT             NULL        COMMENT '소셜 종류_id', 
    `user_social_id`  VARCHAR(50)     NULL        COMMENT '유저_소셜_id', 
    `is_deleted`      TINYINT         NOT NULL    DEFAULT FALSE COMMENT '삭제여부', 
    PRIMARY KEY (user_no)
);

ALTER TABLE users
    ADD CONSTRAINT FK_users_social_id_social_networks_social_network_no FOREIGN KEY (social_id)
        REFERENCES social_networks (social_network_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

INSERT INTO users
(
    user_no,
    name,
    email,
    password
) VALUES (
    1,
    '손수정',
    'soojung@soojung.com',
    123456
);

-- main_categories Table Create SQL
CREATE TABLE main_categories
(
    `main_category_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `name`              VARCHAR(50)    NOT NULL    COMMENT '카테고리명', 
    PRIMARY KEY (main_category_no)
);

ALTER TABLE main_categories COMMENT '1차 카테고리';

INSERT INTO main_categories
(
    main_category_no,
    name
) VALUES (
    1,
    '아우터'
), (
    2,
    '상의'
), (
    3,
    '바지'
), (
    4,
    '원피스'
), (
    5,
    '스커트'
), (
    6,
    '신발'
), (
    7,
    '가방'
), (
    8,
    '주얼리'
), (
    9,
    '잡화'
), (
    10,
    '라이프웨어'
), (
    11,
    '빅사이즈'
);

-- product_options Table Create SQL
CREATE TABLE product_options
(
    `product_option_no`  INT        NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `product_id`         INT        NOT NULL    COMMENT '상품_id', 
    `color_id`           INT        NOT NULL    COMMENT '색상_id', 
    `size_id`            INT        NOT NULL    COMMENT '사이즈_id', 
    `is_deleted`         TINYINT    NOT NULL    DEFAULT FALSE COMMENT '삭제여부', 
    PRIMARY KEY (product_option_no)
);

ALTER TABLE product_options COMMENT '상품_옵션';

ALTER TABLE product_options
    ADD CONSTRAINT FK_product_options_color_id_colors_color_no FOREIGN KEY (color_id)
        REFERENCES colors (color_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE product_options
    ADD CONSTRAINT FK_product_options_size_id_sizes_size_no FOREIGN KEY (size_id)
        REFERENCES sizes (size_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE product_options
    ADD CONSTRAINT FK_product_options_product_id_products_product_no FOREIGN KEY (product_id)
        REFERENCES products (product_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

INSERT INTO product_options
(
    product_option_no,
    product_id,
    color_id,
    size_id
) VALUES (
    1,
    1,
    1,
    1
);

-- user_shipping_details Table Create SQL
CREATE TABLE user_shipping_details
(
    `user_shipping_detail_no`  INT             NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `user_id`                  INT             NOT NULL    COMMENT '유저_id', 
    `address`                  VARCHAR(500)    NOT NULL    COMMENT '배송지', 
    `receiver`                 VARCHAR(50)     NOT NULL    COMMENT '수령자명', 
    `phone_number`             VARCHAR(50)     NOT NULL    COMMENT '휴대폰번호', 
    `delivery_request`         VARCHAR(500)    NULL        COMMENT '배송시 요청사항', 
    PRIMARY KEY (user_shipping_detail_no)
);

ALTER TABLE user_shipping_details
    ADD CONSTRAINT FK_user_shipping_details_user_id_users_user_no FOREIGN KEY (user_id)
        REFERENCES users (user_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

INSERT INTO user_shipping_details
(
    user_shipping_detail_no,
    user_id,
    address,
    receiver,
    phone_number    
) VALUES (
    1,
    1,
    '서울특별시 강남구 테헤란로 32길 26 청송빌딩',
    '위코드',
    '01012345678'
);

-- order_status Table Create SQL
CREATE TABLE order_status
(
    `order_status_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `name`             VARCHAR(50)    NOT NULL    COMMENT '주문상태', 
    PRIMARY KEY (order_status_no)
);

INSERT INTO order_status
(
    order_status_no,
    name
) VALUES (
    1,
    '결제완료'
), (
    2,
    '주문취소'
);

-- orders Table Create SQL
CREATE TABLE orders
(
    `order_no`          INT         NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `user_id`           INT         NOT NULL    COMMENT '유저_id',
    `created_at`        DATETIME    NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시', 
    `is_deleted`        TINYINT     NOT NULL    DEFAULT FALSE COMMENT '삭제여부', 
    PRIMARY KEY (order_no)
);

ALTER TABLE orders
    ADD CONSTRAINT FK_orders_user_id_users_user_no FOREIGN KEY (user_id)
        REFERENCES users (user_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

INSERT INTO orders
(
    order_no,
    user_id
) VALUES (
    1,
    1
);

-- sub_categories Table Create SQL
CREATE TABLE sub_categories
(
    `sub_category_no`   INT            NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `main_category_id`  INT            NOT NULL    COMMENT '1차카테고리_id', 
    `name`              VARCHAR(50)    NOT NULL    COMMENT '카테고리명', 
    PRIMARY KEY (sub_category_no)
);

ALTER TABLE sub_categories COMMENT '2차 카테고리';

ALTER TABLE sub_categories
    ADD CONSTRAINT FK_main_category_no FOREIGN KEY (main_category_id)
        REFERENCES main_categories (main_category_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

INSERT INTO sub_categories
(
    sub_category_no,
    name,
    main_category_id
) VALUES (
    1,
    '자켓',
    1
), (
    2,
    '가디건',
    1
), (
    3,
    '코트',
    1
), ( 
    4,
    '점퍼',
    1
), (
    5,
    '패딩',
    1
), (
    6,
    '무스탕/퍼',
    1
), (
    7,
    '기타',
    1
), (
    8,
    '티셔츠',
    2
), (
    9,
    '셔츠/블라우스',
    2
), (
    10,
    '니트',
    2
), (
    11,
    '후드/맨투맨',
    2
), ( 
    12,
    '베스트',
    2
), (
    13,
    '청바지',
    3
), (
    14,
    '슬랙스',
    3
), (
    15, 
    '면바지',
    3
), ( 
    16, 
    '반바지',
    3
), (
    17, 
    '트레이닝/조거',
    3
), (
    18, 
    '레깅스',
    3
), (
    19, 
    '미니',
    4
), (
    20, 
    '미디',
    4
), (
    21, 
    '롱',
    4
), (
    22, 
    '투피스',
    4
), (
    23, 
    '점프수트',
    4
), ( 
    24,
    '미니',
    5
), (
    25, 
    '미디',
    5
), (
    26, 
    '롱',
    5
), (
    27, 
    '플랫/로퍼',
    6
), ( 
    28, 
    '샌들/슬리퍼',
    6
), (
    29, 
    '힐',
    6
), (
    30, 
    '스니커즈',
    6
), (
    31, 
    '부츠/워커',
    6
), (
    32, 
    '크로스백',
    7
), (
    33, 
    '토트백',
    7
), (
    34, 
    '숄더백',
    7
), (
    35, 
    '에코백',
    7
), ( 
    36, 
    '클러치',
    7
), (
    37, 
    '백팩',
    7
), (
    38, 
    '귀걸이',
    8
), (
    39, 
    '목걸이',
    8
), ( 
    40, 
    '팔찌/발찌',
    8
), (
    41, 
    '반지',
    8
), (
    42, 
    '휴대폰 acc',
    9
), (
    43, 
    '헤어 acc',
    9
), (
    44, 
    '양말/스타킹',
    9
), (
    45, 
    '지갑/파우치',
    9
), (
    46, 
    '모자',
    9
), (
    47, 
    '벨트',
    9
), ( 
    48, 
    '시계',
    9
), (
    49, 
    '스카프',
    9
), (
    50, 
    '머플러',
    9
), (
    51, 
    '아이웨어',
    9
), ( 
    52, 
    '기타',
    9
), (
    53, 
    '언더웨어',
    10
), (
    54,
    '홈웨어',
    10
), (
    55, 
    '스윔웨어',
    10
), (
    56, 
    '비치웨어',
    10
), (
    57,
    '기타',
    10
), (
    58, 
    '아우터',
    11
), (
    59, 
    '상의',
    11
), ( 
    60,
    '바지',
    11
), (
    61, 
    '원피스',
    11
), (
    62, 
    '스커트',
    11
);

-- discount_rate Table Create SQL
CREATE TABLE discount_rate
(
    `discount_rate_no`  INT    NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `rate`              INT    NOT NULL    COMMENT '할인률', 
    PRIMARY KEY (discount_rate_no)
);


-- orders_details Table Create SQL
CREATE TABLE orders_details
(
    `order_detail_no`   INT         NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `order_id`          INT         NOT NULL    COMMENT '주문_id', 
    `user_shipping_id`  INT         NOT NULL    COMMENT '배송지_id', 
    `order_status_id`   INT         NOT NULL    COMMENT '주문상태_id', 
    `start_time`        DATETIME    NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '선분이력관리용(생성)', 
    `close_time`        DATETIME    NOT NULL    DEFAULT '9999-12-31 23:59:59'COMMENT '선분이력관리용(삭제)', 
    PRIMARY KEY (order_detail_no)
);

ALTER TABLE orders_details
    ADD CONSTRAINT FK_user_shipping_detail_no FOREIGN KEY (user_shipping_id)
        REFERENCES user_shipping_details (user_shipping_detail_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE orders_details
    ADD CONSTRAINT FK_orders_details_order_id_orders_order_no FOREIGN KEY (order_id)
        REFERENCES orders (order_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE orders_details
    ADD CONSTRAINT FK_orders_details_order_status_id_order_status_order_status_no FOREIGN KEY (order_status_id)
        REFERENCES order_status (order_status_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

INSERT INTO orders_details
(
    order_detail_no,
    order_id,
    user_shipping_id,
    order_status_id
) VALUES (
    1,
    1,
    1,
    1
);

-- images Table Create SQL
CREATE TABLE images
(
    `image_no`    INT             NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `image`       VARCHAR(500)    NOT NULL    COMMENT '이미지url', 
    `is_deleted`  TINYINT         NOT NULL    DEFAULT FALSE COMMENT '삭제여부', 
    PRIMARY KEY (image_no)
);

INSERT INTO images
(
    image_no,
    image
) VALUES (
    1,
    "http://image.brandi.me/cproduct/2020/07/06/17993567_1594029654_image1_M.jpg"
), (
    2,
    "http://image.brandi.me/cproduct/2020/08/20/16814508_1597899641_image1_M.jpg"
), (
    3,
    "http://image.brandi.me/cproduct/2020/05/31/16896246_1590931916_image1_M.jpg"
), (
    4,
    "http://image.brandi.me/cproduct/2020/05/29/16841528_1590732351_image1_M.jpg"
), (
    5,
    "http://image.brandi.me/cproduct/2020/06/28/17786204_1593354326_image1_M.jpg"
), (
    6,
    "http://image.brandi.me/cproduct/2020/06/21/17426352_1592713625_image1_M.jpg"
), (
    7,
    "http://image.brandi.me/cproduct/2020/05/18/16379275_1589813844_image1_M.jpg"
), (
    8,
    "http://image.brandi.me/cproduct/2020/08/16/18960858_1597566426_image1_M.jpg"
), (
    9,
    "http://image.brandi.me/cproduct/2020/05/19/16448262_1589891341_image1_M.jpg"
), (
    10,
    "http://image.brandi.me/cproduct/2020/06/08/17184315_1591610586_image1_M.jpg"
), (
    11,
    "http://image.brandi.me/cproduct/2020/06/26/17741364_1593101362_image1_M.jpg"
), (
    12,
    "http://image.brandi.me/cproduct/2019/08/01/9907221_1564645496_image1_M.jpg"
), (
    13,
    "http://image.brandi.me/cproduct/2020/08/10/18846870_1597024374_image1_M.jpg"
), (
    14,
    "http://image.brandi.me/cproduct/2020/03/05/5583139_1583400501_image1_M.jpg"
), (
    15,
    "http://image.brandi.me/cproduct/2019/08/19/10059176_1566214986_image1_M.jpg"
), (
    16,
    "http://image.brandi.me/cproduct/2020/04/28/15899675_1588044782_image1_M.jpg"
), (
    17,
    "http://image.brandi.me/cproduct/2020/08/15/18895387_1597493091_image1_M.jpg"
), (
    18,
    "http://image.brandi.me/cproduct/2020/04/09/15346962_1586364000_image1_M.jpg"
), (
    19,
    "http://image.brandi.me/cproduct/2020/07/10/15153293_1594373068_image1_M.jpg"
),(
    20,
    "http://image.brandi.me/cproduct/2020/06/12/17326713_1591894323_image1_M.jpg"
);

-- product_details Table Create SQL
CREATE TABLE product_details
(
    `product_detail_no`    INT              NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `product_id`           INT              NOT NULL    COMMENT '상품_id', 
    `is_activated`         TINYINT          NOT NULL    COMMENT '판매여부', 
    `is_displayed`         TINYINT          NOT NULL    COMMENT '진열여부', 
    `main_category_id`     INT              NOT NULL    COMMENT '1차카테고리', 
    `sub_category_id`      INT              NOT NULL    COMMENT '2차카테고리', 
    `name`                 VARCHAR(100)     NOT NULL    COMMENT '상품명', 
    `simple_description`   VARCHAR(500)     NULL        COMMENT '한줄 상품 설명', 
    `detail_information`   LONGTEXT         NOT NULL    COMMENT '상품상세정보', 
    `price`                DECIMAL(10,2)    NOT NULL    COMMENT '판매가', 
    `discount_rate_id`     INT              NULL        COMMENT '할인률_id', 
    `discount_start_date`  DATETIME         NULL        COMMENT '할인시작일시', 
    `discount_end_date`    DATETIME         NULL        COMMENT '할인종료일시', 
    `min_sales_quantity`   INT              NOT NULL    COMMENT '최소판매수량', 
    `max_sales_quantity`   INT              NOT NULL    COMMENT '최대판매수량', 
    `start_time`           DATETIME         NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '선분이력관리용(생성)', 
    `close_time`           DATETIME         NOT NULL    DEFAULT '9999-12-31 23:59:59' COMMENT '선분이력관리용(삭제)', 
    PRIMARY KEY (product_detail_no)
);

ALTER TABLE product_details
    ADD CONSTRAINT FK_product_details_product_id_products_product_no FOREIGN KEY (product_id)
        REFERENCES products (product_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE product_details
    ADD CONSTRAINT FK_main_category_id FOREIGN KEY (main_category_id)
        REFERENCES main_categories (main_category_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE product_details
    ADD CONSTRAINT FK_sub_category_id FOREIGN KEY (sub_category_id)
        REFERENCES sub_categories (sub_category_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE product_details
    ADD CONSTRAINT FK_discount_rate_id FOREIGN KEY (discount_rate_id)
        REFERENCES discount_rate (discount_rate_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

INSERT INTO product_details
(
    product_detail_no,
    product_id,
    is_activated,
    is_displayed,
    main_category_id,
    sub_category_id,
    name,
    detail_information,
    price,
    min_sales_quantity,
    max_sales_quantity
) VALUES (
    1,
    1,
    1,
    1,
    1,
    1,
    '민자 보트넥 썸머 여리 긴팔 니트 티셔츠',
    '상품 설명',
    14700,
    1,
    20
);

-- product_images Table Create SQL
CREATE TABLE product_images
(
    `product_image_no`  INT         NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `product_id`        INT         NOT NULL    COMMENT '상품상세_id', 
    `image_id`          INT         NOT NULL    COMMENT '이미지_id', 
    `is_main`           TINYINT     NOT NULL    DEFAULT FALSE COMMENT '대표이미지여부', 
    `start_time`        DATETIME    NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '선분이력관리(생성)', 
    `close_time`        DATETIME    NOT NULL    DEFAULT '9999-12-31 23:59:59' COMMENT '선분이력관리(삭제)', 
    PRIMARY KEY (product_image_no)
);

ALTER TABLE product_images COMMENT '상품이미지';

ALTER TABLE product_images
    ADD CONSTRAINT FK_product_images_product_id_products_product_no FOREIGN KEY (product_id)
        REFERENCES products (product_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE product_images
    ADD CONSTRAINT FK_product_images_image_id_images_image_no FOREIGN KEY (image_id)
        REFERENCES images (image_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

INSERT INTO product_images
(
    product_image_no,
    product_id,
    image_id,
    is_main
) VALUES (
    1,
    1,
    1,
    1
);

-- order_product Table Create SQL
CREATE TABLE order_product
(
    `order_product_no`   INT    NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `order_id`           INT    NOT NULL    COMMENT '주문상세_id', 
    `product_option_id`  INT    NOT NULL    COMMENT '상품상세_id', 
    `quantity`           INT    NOT NULL    COMMENT '주문수량', 
    PRIMARY KEY (order_product_no)
);

ALTER TABLE order_product
    ADD CONSTRAINT FK_order_product_order_id_orders_details_order_detail_no FOREIGN KEY (order_id)
        REFERENCES orders_details (order_detail_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE order_product
    ADD CONSTRAINT FK_product_option_id FOREIGN KEY (product_option_id)
        REFERENCES product_options (product_option_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

INSERT INTO order_product
(
    order_product_no,
    order_id,
    product_option_id,
    quantity
) VALUES (
    1,
    1,
    1,
    2
);

-- quantities Table Create SQL
CREATE TABLE quantities
(
    `quantity_no`        INT         NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `product_option_id`  INT         NOT NULL    COMMENT '상품_옵션_id', 
    `quantity`           INT         NOT NULL    COMMENT '재고', 
    `start_time`         DATETIME    NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '선분이력관리용(생성)', 
    `close_time`         DATETIME    NOT NULL    DEFAULT '9999-12-31 23:59:59' COMMENT '선분이력관리용(삭제)', 
    PRIMARY KEY (quantity_no)
);

ALTER TABLE quantities
    ADD CONSTRAINT FK_quantities_product_option_id FOREIGN KEY (product_option_id)
        REFERENCES product_options (product_option_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

INSERT INTO quantities
(
    quantity_no,
    product_option_id,
    quantity
) VALUES (
    1,
    1,
    30
);
