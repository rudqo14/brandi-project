-- products Table Create SQL
CREATE TABLE products
(
    `id`          INT         NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `created_at`  DATETIME    NOT NULL    COMMENT '생성일시', 
    `is_deleted`  TINYINT     NOT NULL    COMMENT '삭제여부', 
    PRIMARY KEY (id)
);


-- products Table Create SQL
CREATE TABLE social_networks
(
    `id`    INT            NOT NULL    AUTO_INCREMENT, 
    `name`  VARCHAR(45)    NOT NULL    COMMENT '소셜 이름', 
    PRIMARY KEY (id)
);


-- products Table Create SQL
CREATE TABLE users
(
    `id`              INT             NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `name`            VARCHAR(50)     NOT NULL      COMMENT '회원명', 
    `email`           VARCHAR(255)    NOT NULL    COMMENT '이메일', 
    `created_at`      DATETIME        NOT NULL    COMMENT '등록일', 
    `last_access`     DATETIME        NOT NULL    COMMENT '최종접속일', 
    `social_id`       INT             NULL        COMMENT '소셜 종류_id', 
    `user_social_id`  VARCHAR(50)     NULL        COMMENT '유저_소셜_id', 
    PRIMARY KEY (id),
    UNIQUE KEY email(email)
);

ALTER TABLE users
    ADD CONSTRAINT FK_users_social_id_social_networks_id FOREIGN KEY (social_id)
        REFERENCES social_networks (id) ON DELETE RESTRICT ON UPDATE RESTRICT;


-- products Table Create SQL
CREATE TABLE main_categories
(
    `id`    INT            NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `name`  VARCHAR(50)    NOT NULL    COMMENT '카테고리명', 
    PRIMARY KEY (id)
);

ALTER TABLE main_categories COMMENT '1차 카테고리';


-- products Table Create SQL
CREATE TABLE user_shipping_details
(
    `id`                INT             NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `user_id`           INT             NOT NULL    COMMENT '유저_id', 
    `address`           VARCHAR(500)    NOT NULL    COMMENT '배송지', 
    `receiver`          VARCHAR(50)     NOT NULL    COMMENT '수령자명', 
    `phone_number`      VARCHAR(50)     NOT NULL    COMMENT '휴대폰번호', 
    `delivery_request`  VARCHAR(500)    NULL        COMMENT '배송시 요청사항', 
    PRIMARY KEY (id)
);

ALTER TABLE user_shipping_details
    ADD CONSTRAINT FK_user_shipping_details_user_id_users_id FOREIGN KEY (user_id)
        REFERENCES users (id) ON DELETE RESTRICT ON UPDATE RESTRICT;


-- products Table Create SQL
CREATE TABLE colors
(
    `id`    INT            NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `name`  VARCHAR(50)    NOT NULL    COMMENT '색상명', 
    PRIMARY KEY (id)
);

ALTER TABLE colors COMMENT '색상 옵션';


-- products Table Create SQL
CREATE TABLE sizes
(
    `id`    INT            NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `name`  VARCHAR(50)    NOT NULL    COMMENT '사이즈명', 
    PRIMARY KEY (id)
);

ALTER TABLE sizes COMMENT '사이즈 옵션';


-- products Table Create SQL
CREATE TABLE order_status
(
    `id`    INT            NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `name`  VARCHAR(50)    NOT NULL    COMMENT '주문상태', 
    PRIMARY KEY (id)
);


-- products Table Create SQL
CREATE TABLE orders
(
    `id`          INT         NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `user_id`     INT         NOT NULL    COMMENT '유저_id', 
    `created_at`  DATETIME    NOT NULL    COMMENT '생성일시', 
    `is_deleted`  TINYINT     NOT NULL    COMMENT '삭제여부', 
    PRIMARY KEY (id)
);

ALTER TABLE orders
    ADD CONSTRAINT FK_orders_user_id_users_id FOREIGN KEY (user_id)
        REFERENCES users (id) ON DELETE RESTRICT ON UPDATE RESTRICT;


-- products Table Create SQL
CREATE TABLE sub_categories
(
    `id`                INT            NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `main_category_id`  INT            NOT NULL    COMMENT '1차카테고리_id', 
    `name`              VARCHAR(50)    NOT NULL    COMMENT '카테고리명', 
    PRIMARY KEY (id)
);

ALTER TABLE sub_categories COMMENT '2차 카테고리';

ALTER TABLE sub_categories
    ADD CONSTRAINT FK_sub_categories_main_category_id_main_categories_id FOREIGN KEY (main_category_id)
        REFERENCES main_categories (id) ON DELETE RESTRICT ON UPDATE RESTRICT;


-- products Table Create SQL
CREATE TABLE discount_rate
(
    `id`    INT    NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `rate`  INT    NOT NULL    COMMENT '할인률', 
    PRIMARY KEY (id)
);


-- products Table Create SQL
CREATE TABLE product_options
(
    `id`          INT         NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `product_id`  INT         NOT NULL    COMMENT '상품_id', 
    `color_id`    INT         NOT NULL    COMMENT '색상_id', 
    `size_id`     INT         NOT NULL    COMMENT '사이즈_id', 
    `quantity`    INT         NULL        COMMENT '재고 수량', 
    `updated_at`  DATETIME    NULL        COMMENT '선분생성일시', 
    `start_time`  DATETIME    NOT NULL    COMMENT '선분이력관리용(생성)', 
    `close_time`  DATETIME    NOT NULL    COMMENT '선분이력관리용(삭제)', 
    PRIMARY KEY (id)
);

ALTER TABLE product_options COMMENT '상품_옵션';

ALTER TABLE product_options
    ADD CONSTRAINT FK_product_options_color_id_colors_id FOREIGN KEY (color_id)
        REFERENCES colors (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE product_options
    ADD CONSTRAINT FK_product_options_size_id_sizes_id FOREIGN KEY (size_id)
        REFERENCES sizes (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE product_options
    ADD CONSTRAINT FK_product_options_product_id_products_id FOREIGN KEY (product_id)
        REFERENCES products (id) ON DELETE RESTRICT ON UPDATE RESTRICT;


-- products Table Create SQL
CREATE TABLE orders_information
(
    `id`                INT         NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `order_id`          INT         NOT NULL    COMMENT '주문_id', 
    `user_shipping_id`  INT         NOT NULL    COMMENT '배송지_id', 
    `order_status_id`   INT         NOT NULL    COMMENT '주문상태_id', 
    `updated_at`        DATETIME    NULL        COMMENT '선분생성일시', 
    `start_time`        DATETIME    NOT NULL    COMMENT '선분이력관리용(생성)', 
    `close_time`        DATETIME    NOT NULL    COMMENT '선분이력관리용(삭제)', 
    PRIMARY KEY (id)
);

ALTER TABLE orders_information
    ADD CONSTRAINT FK_orders_information_user_shipping_id_user_shipping_details_id FOREIGN KEY (user_shipping_id)
        REFERENCES user_shipping_details (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE orders_information
    ADD CONSTRAINT FK_orders_information_order_id_orders_id FOREIGN KEY (order_id)
        REFERENCES orders (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE orders_information
    ADD CONSTRAINT FK_orders_information_order_status_id_order_status_id FOREIGN KEY (order_status_id)
        REFERENCES order_status (id) ON DELETE RESTRICT ON UPDATE RESTRICT;


-- products Table Create SQL
CREATE TABLE images
(
    `id`          INT             NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `image`       VARCHAR(500)    NOT NULL    COMMENT '이미지url', 
    `is_deleted`  TINYINT         NOT NULL    COMMENT '삭제여부', 
    PRIMARY KEY (id)
);


-- products Table Create SQL
CREATE TABLE product_information
(
    `id`                   INT              NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `product_id`           INT              NOT NULL    COMMENT '상품_id', 
    `is_activated`         TINYINT          NOT NULL    COMMENT '판매여부', 
    `is_displayed`         TINYINT          NOT NULL    COMMENT '진열여부', 
    `main_category_id`     INT              NOT NULL    COMMENT '1차카테고리', 
    `sub_category_id`      INT              NOT NULL    COMMENT '2차카테고리', 
    `name`                 VARCHAR(100)     NOT NULL    COMMENT '상품명', 
    `simple_description`   VARCHAR(500)     NOT NULL    COMMENT '한줄 상품 설명', 
    `detail_information`   LONGTEXT         NOT NULL    COMMENT '상품상세정보', 
    `price`                DECIMAL(10,2)    NOT NULL    COMMENT '판매가', 
    `discount_rate_id`     INT              NULL        COMMENT '할인률_id', 
    `discount_start_date`  DATETIME         NULL        COMMENT '할인시작일시', 
    `discount_end_date`    DATETIME         NULL        COMMENT '할인종료일시', 
    `min_sales_quantity`   INT              NOT NULL    COMMENT '최소판매수량', 
    `max_sales_quantity`   INT              NOT NULL    COMMENT '최대판매수량', 
    `updated_at`           DATETIME         NULL        COMMENT '선분생성일시', 
    `start_time`           DATETIME         NOT NULL    COMMENT '선분이력관리용(생성)', 
    `close_time`           DATETIME         NOT NULL    COMMENT '선분이력관리용(삭제)', 
    PRIMARY KEY (id)
);

ALTER TABLE product_information
    ADD CONSTRAINT FK_product_information_product_id_products_id FOREIGN KEY (product_id)
        REFERENCES products (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE product_information
    ADD CONSTRAINT FK_product_information_main_category_id_main_categories_id FOREIGN KEY (main_category_id)
        REFERENCES main_categories (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE product_information
    ADD CONSTRAINT FK_product_information_sub_category_id_sub_categories_id FOREIGN KEY (sub_category_id)
        REFERENCES sub_categories (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE product_information
    ADD CONSTRAINT FK_product_information_discount_rate_id_discount_rate_id FOREIGN KEY (discount_rate_id)
        REFERENCES discount_rate (id) ON DELETE RESTRICT ON UPDATE RESTRICT;


-- products Table Create SQL
CREATE TABLE product_images
(
    `id`                      INT         NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `product_infromation_id`  INT         NOT NULL    COMMENT '상품상세_id', 
    `image_id`                INT         NOT NULL    COMMENT '이미지_id', 
    `is_main`                 TINYINT     NOT NULL    COMMENT '대표이미지여부', 
    `updated_at`              DATETIME    NULL        COMMENT '선분생성일시', 
    `start_time`              DATETIME    NOT NULL    COMMENT '선분이력관리용(생성)', 
    `close_time`              DATETIME    NOT NULL    COMMENT '선분이력관리용(삭제)', 
    PRIMARY KEY (id)
);

ALTER TABLE product_images COMMENT '상품이미지';

ALTER TABLE product_images
    ADD CONSTRAINT FK_product_images_product_infromation_id_products_id FOREIGN KEY (product_infromation_id)
        REFERENCES products (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE product_images
    ADD CONSTRAINT FK_product_images_image_id_images_id FOREIGN KEY (image_id)
        REFERENCES images (id) ON DELETE RESTRICT ON UPDATE RESTRICT;


-- products Table Create SQL
CREATE TABLE order_product
(
    `id`                 INT    NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `order_id`           INT    NOT NULL    COMMENT '주문상세_id', 
    `product_option_id`  INT    NOT NULL    COMMENT '상품상세_id', 
    `quantity`           INT    NOT NULL    COMMENT '주문수량', 
    PRIMARY KEY (id)
);

ALTER TABLE order_product
    ADD CONSTRAINT FK_order_product_order_id_orders_information_id FOREIGN KEY (order_id)
        REFERENCES orders_information (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE order_product
    ADD CONSTRAINT FK_order_product_product_option_id_product_options_id FOREIGN KEY (product_option_id)
        REFERENCES product_options (id) ON DELETE RESTRICT ON UPDATE RESTRICT;



