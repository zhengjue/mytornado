# _*_ coding:utf-8 _*_

# 男性 女性 其他
MALE = 0
FEMALE = 1
OTHER = 2

SEX_LIST = [MALE, FEMALE, OTHER]

# 请假 加薪 报销
TRANSACTION_TYPE_LEAVE = 0
TRANSACTION_TYPE_RAISE = 1
TRANSACTION_TYPE_REIMBURSEMENT = 2

TRANSACTION_TYPE_LIST = [TRANSACTION_TYPE_LEAVE, TRANSACTION_TYPE_RAISE, TRANSACTION_TYPE_REIMBURSEMENT]

# 非管理人 事业集群负责人 事业负责人 学院负责人
NORMAL = "normal"
CLUSTER = "cluster"
BUSINESS = "buiness"
ACADEMY = "academy"

ADMIN_USER_PERMISSION_LIST = [CLUSTER, BUSINESS, ACADEMY]