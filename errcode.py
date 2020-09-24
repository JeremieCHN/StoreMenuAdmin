OK = 0
COMMON = 1

# 登录相关
LOGIN_FAILED = 2
NEED_LOGIN = 3

# 管理相关

# 不存在
GOOD_NOT_EXISTS = 4
TYPE_NOT_EXISTS = 5
IMAGE_NOT_EXISTS = 6

# 重复
TYPE_NAME_REPEATED = 7

MSG_MAP = {
    COMMON : "非法参数",

    GOOD_NOT_EXISTS : "该商品不存在",
    TYPE_NOT_EXISTS : "该类型不存在",
    IMAGE_NOT_EXISTS : "该图片不存在",

    TYPE_NAME_REPEATED: "类型名重复",
}
