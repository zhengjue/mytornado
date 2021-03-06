# _*_ coding:utf-8 _*_

# 男性 女性 其他
MALE = 1
FEMALE = 2
OTHER = 3

SEX_LIST = [MALE, FEMALE, OTHER]
SEX_DICT = {
    MALE: u'男',
    FEMALE: u'女',
    OTHER: u'其他'
}

# 请假 加薪 报销
TRANSACTION_TYPE_LEAVE = 0
TRANSACTION_TYPE_RAISE = 1
TRANSACTION_TYPE_REIMBURSEMENT = 2

TRANSACTION_TYPE_LIST = [TRANSACTION_TYPE_LEAVE, TRANSACTION_TYPE_RAISE, TRANSACTION_TYPE_REIMBURSEMENT]
TRANSACTION_TYPE_DICT = {
    TRANSACTION_TYPE_LEAVE: "请假",
    TRANSACTION_TYPE_RAISE: "加薪",
    TRANSACTION_TYPE_REIMBURSEMENT: "报销",

}

PROGRESS_REJECT = 0  # 0为驳回
PROGRESS_CREATE = 1  # 1 为创建状态
PROGRESS_ACADEMY = 2  # 2为学院负责人审核通过
PROGRESS_BUSINESS = 3  # 3为事业群负责人审核通过
PROGRESS_CLUSTER = 4  # 4为事业集群负责人审核通过

PROGRESS_LIST = [PROGRESS_REJECT, PROGRESS_CREATE, PROGRESS_ACADEMY, PROGRESS_BUSINESS, PROGRESS_CLUSTER]
PROGRESS_DICT = {
    PROGRESS_REJECT: "驳回",
    PROGRESS_CREATE: "创建状态",
    PROGRESS_ACADEMY: "学院负责人审核通过",
    PROGRESS_BUSINESS: "事业群负责人审核通过",
    PROGRESS_CLUSTER: "事业集群负责人审核通过"
}

# 非管理人 事业集群负责人 事业负责人 学院负责人
NORMAL = "normal"
CLUSTER = "cluster"
BUSINESS = "buiness"
ACADEMY = "academy"

ADMIN_USER_PERMISSION_LIST = [CLUSTER, BUSINESS, ACADEMY]

USER_STATUS_NORMAL = 1
USER_STATUS_CHECK = 2
USER_STATUS_NOPASS = 3
USER_STATUS_FORBID = 4
USER_STATUS_DELETE = 5
USER_STATUS_LIST = [USER_STATUS_NORMAL, USER_STATUS_CHECK, USER_STATUS_NOPASS, USER_STATUS_FORBID, USER_STATUS_DELETE]

USER_STATUS_DICT = {
    USER_STATUS_NORMAL: u"正常",
    USER_STATUS_CHECK: u"待审核",
    USER_STATUS_NOPASS: u"没通过",
    USER_STATUS_FORBID: u"禁用",
    USER_STATUS_DELETE: u"已删除"
}
