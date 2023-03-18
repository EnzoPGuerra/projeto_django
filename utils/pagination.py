import math
from django.core.paginator import Paginator

def make_pagination_range(
            page_range,
            qt_pages,
            current_page,
        ):
    
    middlePoint = math.ceil(qt_pages/2)
    range_start = current_page-middlePoint
    range_finish = current_page+middlePoint
    range_length = len(page_range)

    start_range_offset = abs(range_start) if range_start < 0 else 0

    if range_start < 0: 
        range_start = 0
        range_finish += start_range_offset

    if range_finish >= range_length:
        range_start=range_start-abs(range_length-range_finish)


    pagination = page_range[range_start:range_finish]

    return {
        'pagination': pagination,
        'page_range': page_range,
        'qt_pages': qt_pages,
        'current_page': current_page,
        'total_pages': range_length,
        'start_range': range_start,
        'stop_range': range_finish,
        'first_page_out_of_range': current_page > middlePoint,
        'last_page_out_of_range': current_page < (range_length - middlePoint)
    }

def make_pagination(request, querySet, per_page, qt_pages=4):
    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError: 
        current_page = 1

    paginator = Paginator(querySet, per_page)
    page_obj = paginator.get_page(current_page)

    pagination_range = make_pagination_range(
        page_range=paginator.page_range,
        current_page=current_page,
        qt_pages=qt_pages
    )

    return page_obj, pagination_range