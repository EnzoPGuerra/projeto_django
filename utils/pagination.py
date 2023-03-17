import math

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