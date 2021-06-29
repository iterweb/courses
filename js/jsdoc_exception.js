// документация для функции
/**
 * Преобразование строки со временем в минуты
 * @param {string} time время в виде строки, например "02:08"
 * @return {number} целое число в минутах, например time="02:08", вернет 128
 */

function timeToMinute(time) {
    try {
        let hour = +time.split(":")[0]
        let minute = +time.split(":")[1]

        if (!(hour >= 0 && hour <= 23) || !(minute >= 0 && minute <= 59)) {
            throw new RangeError("Аргумент в формате hh:mm, hh - число от 0 до 23, а mm - число от 0 до 59")
        }
        return hour * 60 + minute
    }
    catch (e) {
        console.log(e)
    }
}

console.log(timeToMinute("24:08"))