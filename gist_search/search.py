from gist_search.utils import get_gists


def search_gists(username, description=None, file_name=None):
    if not description and not file_name:
        print("At least one search parameter must be specified")
        return
    
    gists = get_gists(username)
    results = []
    
    for gist in gists :
        if description and description.lower() not in gist['description'].lower() :
            continue
        
        if file_name :
            matched = False
            for k,v in gist['files'].items():
                if file_name.lower() in k.lower():
                    matched = True
            if not matched:
                continue
        
        results.append(gist)
    print(len(results))
    return results