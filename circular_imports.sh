# echo '' > directional_data.txt
echo "path;eachline;pythonifiedpath;importedmodule" > directional_data.txt
git ls-files | grep '.py$' > file_names.txt
while IFS=';' read -r path || [[ -n "$path" ]]; do
    foundstrs=$(cat $path | grep import)
    while read -r eachline; do
        if ! [[ $eachline =~ .*#.*import.* ]]; then
            if [[ $eachline =~ .*from.* ]]; then
                importedmodule=$(echo `expr "$eachline" : 'from \(.*\) import.*'`)
            else
                importedmodule=$(echo `expr "$eachline" : 'import \(.*\)'`)
            fi
            pythonifiedpath=$(echo `expr "$path" : '\./\(.*\)\.py'` | sed -e 's/\//\./g')
            echo "$path\t$eachline\t$pythonifiedpath\t$importedmodule" >> directional_data.txt
        fi
    done <<< "$foundstrs"
done < "file_names.txt"