"""
自定義
"""
from django.utils.safestring import mark_safe


class Pagination(object):
    def __init__(self, request, queryset, page_size=10, page_param="page", plus=5):

        import copy
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict

        self.page_param = page_param
        page = request.GET.get(page_param, "1")
        if page.isdecimal():
            page = int(page)
        else:
            page = 1
        self.page = page
        self.page_size = page_size
        self.start = (page - 1) * page_size
        self.end = page * page_size
        self.page_queryset = queryset[self.start:self.end]

        total_count = queryset.count()
        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.plus = plus

    def html(self):
        # 頁碼
        if self.total_page_count <= 2 * self.plus + 1:
            start_page = 1
            end_page = self.total_page_count
        else:
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1
            else:
                if (self.page + self.plus) > self.total_page_count:
                    start_page = self.total_page_count - 2 * self.plus
                    end_page = self.total_page_count
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus
        page_str_list = []

        self.query_dict.setlist(self.page_param, [1])
        page_str_list.append('<li><a href="?{}">首頁</a></li>'.format(self.query_dict.urlencode()))
        if self.page == 1:
            self.query_dict.setlist(self.page_param, [1])
            prev = '<li><a href="?{}">上一頁</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [self.page - 1])
            prev = '<li><a href="?{}">上一頁</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(prev)
        for i in range(start_page, end_page + 1):
            if i == self.page:
                self.query_dict.setlist(self.page_param, [i])
                ele = '<li class="active"><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            else:
                self.query_dict.setlist(self.page_param, [i])
                ele = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            page_str_list.append(ele)
        if self.page == self.total_page_count:
            self.query_dict.setlist(self.page_param, [self.total_page_count])
            prev = '<li><a href="?{}">下一頁</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [self.page - 1])
            prev = '<li><a href="?{}">下一頁</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(prev)
        self.query_dict.setlist(self.page_param, [self.total_page_count])
        page_str_list.append('<li><a href="?{}">尾頁</a></li>'.format(self.query_dict.urlencode()))

        search_data = """
            <li>
                <form method="get" style="float: left;margin-left: -1px">
                    <input type="text"
                           style="position: relative;float: left;display: inline-block;width: 80px;border-radius: 0"
                           name="page" class="form-control" placeholder="頁碼">
                    <button style="border-radius: 0" class="btn btn-default" type="submit">跳轉</button>
                </form>
            </li>
        """
        page_str_list.append(search_data)
        page_string = mark_safe("".join(page_str_list))
        return page_string
