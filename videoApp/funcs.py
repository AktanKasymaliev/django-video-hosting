from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models.query import QuerySet
from django.http import HttpRequest

def make_pagination(request: HttpRequest, all_data: QuerySet, 
                    context: dict, context_name: str, number_of_content_pre_page: int) -> dict:
                    
    paginator = Paginator(all_data, number_of_content_pre_page)
    page = request.GET.get('page', 1)
    context["page"] = page
    try:
        context[context_name] = paginator.page(page)
    except PageNotAnInteger:
        context[context_name] = paginator.page(1)
    except EmptyPage:
        context[context_name] = paginator.page(paginator.num_pages)
    return context