echo "path;eachline;importedmodule" > directional_data.txt
git ls-files --full-name | grep '.py$' > file_names.txt
while IFS=';' read -r path || [[ -n "$path" ]]; do
    foundstrs=$(cat $path | grep import)
    while read -r eachline; do
        if ! [[ $eachline =~ .*#.*import.* ]]; then
            if [[ $eachline =~ .*from.* ]]; then
                importedmodule=$(echo `expr "$eachline" : 'from \(.*\) import.*'`)
            else
                importedmodule=$(echo `expr "$eachline" : 'import \(.*\)'`)
            fi
            echo -e "$path;$eachline;$importedmodule" >> directional_data.txt
        fi
    done <<< "$foundstrs"
done < "file_names.txt"